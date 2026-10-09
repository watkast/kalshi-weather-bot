# Range-Scalp Bot

*Updated Fri Oct 09 09:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8896 | 7692 | 1204 (13) | 5 | $-2943.27 | -5.2% |
| **+10¢** | 6731 | 5318 | 1413 (25) | 6 | $-2832.81 | -6.7% |
| **+15¢** | 5680 | 4192 | 1488 (37) | 6 | $-2307.17 | -6.5% |
| **+20¢** | 5054 | 3510 | 1544 (45) | 7 | $-1903.38 | -6.0% |
| **+10¢ (15¢ stop)** | 10845 | 10815 | 30 (19) | 4 | $-4072.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 09:52 | +10 stop | ETH | DOWN | 0.59 | open |  |
| 10-09 09:52 | +10 stop | DOGE | UP | 0.57 | open |  |
| 10-09 09:52 | +20 | DOGE | UP | 0.57 | open |  |
| 10-09 09:52 | +15 | DOGE | UP | 0.57 | open |  |
| 10-09 09:52 | +10 | DOGE | UP | 0.57 | open |  |
| 10-09 09:52 | +5 | DOGE | UP | 0.57 | 0.64 | 0.35 |
| 10-09 09:52 | +10 stop | HYPE | UP | 0.60 | open |  |
| 10-09 09:52 | +5 | HYPE | UP | 0.60 | open |  |
| 10-09 09:51 | +5 | ETH | UP | 0.54 | open |  |
| 10-09 09:51 | +10 stop | SOL | DOWN | 0.60 | open |  |
| 10-09 09:50 | +5 | ETH | UP | 0.51 | 0.56 | 0.14 |
| 10-09 09:50 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-09 09:50 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 10-09 09:50 | +20 | HYPE | UP | 0.71 | open |  |
| 10-09 09:50 | +15 | HYPE | UP | 0.71 | open |  |
| 10-09 09:50 | +10 | HYPE | UP | 0.71 | open |  |
| 10-09 09:50 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 10-09 09:50 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.91 |
| 10-09 09:50 | +10 stop | ETH | UP | 0.64 | 0.44 | -2.35 |
| 10-09 09:49 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.22 |
| 10-09 09:49 | +10 stop | DOGE | DOWN | 0.58 | 0.41 | -2.05 |
| 10-09 09:49 | +10 stop | ETH | DOWN | 0.42 | 0.54 | 0.84 |
| 10-09 09:49 | +10 stop | SOL | DOWN | 0.53 | 0.63 | 0.65 |
| 10-09 09:47 | +10 stop | SOL | UP | 0.64 | 0.42 | -2.55 |
| 10-09 09:47 | +20 | SOL | UP | 0.64 | open |  |
| 10-09 09:47 | +15 | SOL | UP | 0.64 | open |  |
| 10-09 09:47 | +10 | SOL | UP | 0.64 | open |  |
| 10-09 09:47 | +5 | SOL | UP | 0.64 | open |  |
| 10-09 09:46 | +10 stop | NEAR | UP | 0.60 | 0.36 | -2.74 |
| 10-09 09:46 | +20 | NEAR | UP | 0.60 | open |  |
| 10-09 09:46 | +15 | NEAR | UP | 0.60 | open |  |
| 10-09 09:46 | +10 | NEAR | UP | 0.60 | open |  |
| 10-09 09:46 | +5 | NEAR | UP | 0.60 | open |  |
| 10-09 09:46 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-09 09:46 | +20 | BNB | UP | 0.59 | 0.82 | 2.02 |
| 10-09 09:46 | +15 | BNB | UP | 0.59 | 0.77 | 1.50 |
| 10-09 09:46 | +10 | BNB | UP | 0.59 | 0.71 | 0.88 |
| 10-09 09:46 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-09 09:46 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-09 09:46 | +20 | HYPE | UP | 0.57 | 0.78 | 1.79 |
