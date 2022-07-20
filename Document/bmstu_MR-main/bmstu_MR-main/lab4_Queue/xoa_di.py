class Modeller:
    def __init__(self, uniform_a, uniform_b, normal_mu, normal_sigma, reenter_prop):
        self._generator = RequestGenerator(UniformGenerator(uniform_a, uniform_b))
        self._processor = RequestProcessor(ErlangGenerator(normal_mu, normal_sigma), reenter_prop)
        self._generator.add_receiver(self._processor)

    def event_based_modelling(self, request_count):
        generator = self._generator
        processor = self._processor

        gen_period = generator.next_time_period()
        proc_period = gen_period + processor.next_time_period()
        while processor.processed_requests < request_count:
            if gen_period <= proc_period:
                generator.emit_request()
                gen_period += generator.next_time_period()
            else:
                processor.process()
                if processor.current_queue_size > 0:
                    proc_period += processor.next_time_period()
                else:
                    proc_period = gen_period + processor.next_time_period()

        return (processor.processed_requests, processor.reentered_requests,
                processor.max_queue_size, proc_period)

    def time_based_modelling(self, request_count, dt):
        generator = self._generator
        processor = self._processor

        gen_period = generator.next_time_period()

        proc_period = gen_period + processor.next_time_period()
        current_time = 0
        while processor.processed_requests < request_count:
            if gen_period <= current_time:
                generator.emit_request()
                gen_period += generator.next_time_period()
            if current_time >= proc_period:
                processor.process()
                if processor.current_queue_size > 0:
                    proc_period += processor.next_time_period()
                else:
                    proc_period = gen_period + processor.next_time_period()
            current_time += dt

        return processor.processed_requests, processor.reentered_requests, processor.max_queue_size, current_time
