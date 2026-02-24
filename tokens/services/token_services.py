from ..serializer import TokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from base.services import ServiceBase
from ..models import Token
from django.utils import timezone

class TokenServices(ServiceBase):
    manager = Token.objects

    @staticmethod
    def generateToken(data):
        serializer = TokenSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            # Generate JWTs
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            # Store lifecycle in DB
            token = TokenServices.create(
                user=user,
                key=access,
                refresh_key=str(refresh),
                expires_at=timezone.now() + timezone.timedelta(minutes=15)
            )

            return {"success": True,
                "data": {"user": serializer.data,"refresh": token.refresh_key,
                    "access": token.key,
                    "expires_at": token.expires_at,
                },
            }

        return { "success": False,"errors": serializer.errors,
        }
    
    @staticmethod
    def refreshToken(refresh_key):
        token = TokenServices.get(refresh_key=refresh_key)
        if not token:
            return {"success": False, "errors": {"error": "Token not found"}}
        if token.revoked or token.is_expired():
            return {"success": False, "errors": {"error": "Invalid or expired refresh token"}}

        # Issue new access token
        refresh = RefreshToken(token.user)
        new_access = str(refresh.access_token)

        # Update lifecycle using ServiceBase.update
        updated = TokenServices.update(
            token,
            key=new_access,
            refreshed_at=timezone.now(),
            expires_at=timezone.now() + timezone.timedelta(minutes=15),
        )

        return {
            "success": True,
            "data": {
                "refresh": updated.refresh_key,
                "access": updated.key,
                "expires_at": updated.expires_at,
            },
        }

    @staticmethod
    def revokeToken(token_id):
        token = TokenServices.get(id=token_id)
        if not token:
            return {"success": False, "errors": {"error": "Token not found"}}

        # Mark token as revoked
        updated = TokenServices.update(token, revoked=True)
        return {"success": True, "data": {"revoked": updated.revoked}}

    @staticmethod
    def deleteToken(token_id):
        token = TokenServices.get(id=token_id)
        if not token:
            return {"success": False, "errors": {"error": "Token not found"}}

        TokenServices.delete(token)
        return {"success": True, "data": {"deleted": True}}
