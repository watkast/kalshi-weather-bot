# Range-Scalp Bot

*Updated Sun Oct 25 01:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32324 | 28185 | 4139 (41) | 0 | $-9210.87 | -4.5% |
| **+10¢** | 24201 | 19407 | 4794 (59) | 0 | $-8250.88 | -5.4% |
| **+15¢** | 20267 | 15112 | 5155 (82) | 0 | $-7370.30 | -5.8% |
| **+20¢** | 17954 | 12561 | 5393 (104) | 0 | $-6503.04 | -5.8% |
| **+10¢ (15¢ stop)** | 39718 | 39658 | 60 (32) | 0 | $-15164.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 01:04 | +10 stop | ZEC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-25 01:04 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 10-25 01:04 | +15 | NEAR | DOWN | 0.71 | 0.88 | 1.47 |
| 10-25 01:04 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 01:04 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 10-25 01:03 | +5 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-25 01:03 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-25 01:01 | +10 stop | ZEC | DOWN | 0.64 | 0.44 | -2.35 |
| 10-25 01:01 | +20 | ZEC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-25 01:01 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-25 01:01 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 01:01 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-25 01:01 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 01:01 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.89 |
| 10-25 01:01 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-25 01:01 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-25 01:01 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-25 01:01 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 01:01 | +20 | DOGE | DOWN | 0.68 | 0.93 | 2.30 |
| 10-25 01:01 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-25 01:01 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-25 01:01 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-25 01:01 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +20 | NEAR | DOWN | 0.62 | 0.88 | 2.35 |
| 10-25 01:01 | +15 | NEAR | DOWN | 0.62 | 0.79 | 1.41 |
| 10-25 01:01 | +10 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 01:01 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 01:01 | +20 | HYPE | DOWN | 0.69 | 0.91 | 1.95 |
| 10-25 01:01 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 01:01 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 01:01 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-25 00:56 | +10 stop | HYPE | UP | 0.29 | 0.56 | 2.37 |
| 10-25 00:56 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 00:56 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-25 00:56 | +15 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-25 00:56 | +10 | NEAR | DOWN | 0.67 | 0.81 | 1.13 |
| 10-25 00:56 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 10-25 00:55 | +10 stop | ETH | UP | 0.61 | 0.85 | 2.14 |
| 10-25 00:55 | +20 | ETH | UP | 0.61 | 0.85 | 2.14 |
