from typing import TYPE_CHECKING

from ...utils import (
    DIFFUSERS_SLOW_IMPORT,
    OptionalDependencyNotAvailable,
    _LazyModule,
    get_objects_from_module,
    is_torch_available,
    is_transformers_available,
)


_dummy_objects = {}
_additional_imports = {}
_import_structure = {"pipeline_output": ["FluxPipelineOutput"]}

try:
    if not (is_transformers_available() and is_torch_available()):
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    from ...utils import dummy_torch_and_transformers_objects  # noqa F403

    _dummy_objects.update(get_objects_from_module(dummy_torch_and_transformers_objects))
else:
    _import_structure["pipeline_flux"] = ["FluxPipeline"]
    _import_structure["pipeline_flux_controlnet"] = ["FluxControlNetPipeline"]
    _import_structure["pipeline_flux_controlnet_image_to_image"] = ["FluxControlNetImg2ImgPipeline"]
    _import_structure["pipeline_flux_controlnet_inpainting"] = ["FluxControlNetInpaintPipeline"]
    _import_structure["pipeline_flux_fill"] = ["FluxFillPipeline"]
    _import_structure["pipeline_flux_img2img"] = ["FluxImg2ImgPipeline"]
    _import_structure["pipeline_flux_inpaint"] = ["FluxInpaintPipeline"]
if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    try:
        if not (is_transformers_available() and is_torch_available()):
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        from ...utils.dummy_torch_and_transformers_objects import *  # noqa F403
    else:
        from .pipeline_flux import FluxPipeline
        from .pipeline_flux_controlnet import FluxControlNetPipeline
        from .pipeline_flux_controlnet_image_to_image import FluxControlNetImg2ImgPipeline
        from .pipeline_flux_controlnet_inpainting import FluxControlNetInpaintPipeline
        from .pipeline_flux_fill import FluxFillPipeline
        from .pipeline_flux_img2img import FluxImg2ImgPipeline
        from .pipeline_flux_inpaint import FluxInpaintPipeline
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )

    for name, value in _dummy_objects.items():
        setattr(sys.modules[__name__], name, value)
    for name, value in _additional_imports.items():
        setattr(sys.modules[__name__], name, value)
