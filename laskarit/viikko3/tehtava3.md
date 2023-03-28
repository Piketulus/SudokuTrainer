```mermaid
    sequenceDiagram
        Main->>Machine: Machine()
        Machine->>FuelTank: FuelTank()
        Machine->>FuelTank: tank.fill(40)
        Machine->>Engine: Engine(self._tank)
        Main->>Machine: drive()
        activate Machine
        Machine->>Engine: start()
        Engine->>FuelTank: consume(5)
        Machine->>Engine: engine.is_running()
        activate Engine
        Engine->>FuelTank: fuel_contents
        FuelTank-->>Engine: 35
        Engine-->>Machine: isRunning=True
        deactivate Engine
        deactivate Machine
        Machine->>Engine: engine.use_energy()
        Engine->>FuelTank: consume(10)
        
```
