from fastapi import APIRouter
from repository.schemas.package_schemas import PackagesSchema
from service.trip_package.package_service import PackageService

package_router = APIRouter()

@package_router.post('/packages/create')
async def create_packages(package: PackagesSchema):
    return await PackageService.create_package(package)

@package_router.get('/packages/{package_id}')
async def get_package(package_id: str):
    return await PackageService.get_package(package_id)

@package_router.put('/packages/update/{package_id}')
async def update_package(package_id: str):
    return await PackageService.update_package(package_id)
