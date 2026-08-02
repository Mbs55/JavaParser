---
source: request post processors
---

# request post processors

# SecurityMockMvcRequestPostProcessors
Spring MVC Test provides a convenient interface (`RequestPostProcessor`) that you can use to modify a request.
Spring Security provides a number of `RequestPostProcessor` implementations that make testing easier.
To use Spring Security's `RequestPostProcessor` implementations, use the following static import:

======
Java::
+
----
import static org.springframework.security.test.web.servlet.request.SecurityMockMvcRequestPostProcessors.*;
----

Kotlin::
+
----
import org.springframework.security.test.web.servlet.request.SecurityMockMvcRequestPostProcessors.*
----
======
