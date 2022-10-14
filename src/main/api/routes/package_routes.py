from fastapi import APIRouter
from repository.schemas.package_schemas import PackagesSchema, DestinationsDTO
from model.trip_package.package_model import DecolarDestinations
from service.trip_package.package_service import PackageService

package_router = APIRouter()

@package_router.get('/packages/destinations')
async def get_destinations():
    result = DestinationsDTO(destinations = [(i.name, i.value) for i in DecolarDestinations])
    return result


@package_router.get('/packages/{package_id}')
async def get_package(package_id: str):
    return await PackageService.get_package(package_id)


@package_router.post('/packages/create')
async def create_packages(package: PackagesSchema):
    return await PackageService.create_package(package)


@package_router.post('/packages/update/{package_id}')
async def update_package(package_id: str):
    return await PackageService.update_package(package_id)

