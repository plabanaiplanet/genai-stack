from fastapi import APIRouter, Response
from typing import Dict, List, Union

from genai_stack.constant import API, STACK
from genai_stack.genai_server.services.stack_service import StackService
from genai_stack.genai_server.models.stack_models import StackRequestModel, StackResponseModel, StackFilterModel, StackUpdateRequestModel
from genai_stack.genai_server.models.delete_model import DeleteResponseModel
from genai_stack.genai_server.models.not_found_model import NotFoundResponseModel
from genai_stack.genai_server.models.bad_request_model import BadRequestResponseModel
from genai_stack.genai_server.database import initialize_store


store = initialize_store()

service = StackService(store=store)

router = APIRouter(
    prefix=API + STACK,
    tags=['stack']
)

@router.post("")
def create_stack(stack:StackRequestModel) -> StackResponseModel:
    return service.create_stack(stack=stack)

@router.get("")
def list_stack() -> Dict[str, List[StackResponseModel]]:
    return service.list_stack()

@router.get("/{stack_id}") 
def get_stack(stack_id:int, response:Response) -> Union[StackResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.get_stack(filter, response)  

@router.delete("/{stack_id}")
def delete_stack(stack_id:int, response:Response) -> Union[DeleteResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.delete_stack(filter, response)   

@router.patch("/{stack_id}")
def update_stack(stack_id:int, stack:StackUpdateRequestModel, response:Response) -> Union[
    StackResponseModel, BadRequestResponseModel, NotFoundResponseModel]:
    filter = StackFilterModel(id=stack_id)
    return service.update_stack(filter, stack, response)