# Range-Scalp Bot

*Updated Wed Oct 07 23:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6956 | 6035 | 921 (13) | 0 | $-2099.16 | -4.8% |
| **+10¢** | 5277 | 4199 | 1078 (20) | 0 | $-1985.26 | -6.0% |
| **+15¢** | 4428 | 3292 | 1136 (27) | 0 | $-1631.98 | -5.9% |
| **+20¢** | 3955 | 2771 | 1184 (34) | 0 | $-1298.55 | -5.2% |
| **+10¢ (15¢ stop)** | 8424 | 8402 | 22 (14) | 0 | $-2966.46 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 23:20 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 10-07 23:20 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 10-07 23:20 | +15 | NEAR | DOWN | 0.66 | 0.84 | 1.54 |
| 10-07 23:20 | +10 | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 10-07 23:20 | +5 | NEAR | DOWN | 0.66 | 0.80 | 1.13 |
| 10-07 23:03 | +10 stop | ETH | UP | 0.51 | no | -5.28 |
| 10-07 23:03 | +20 | ETH | UP | 0.51 | no | -5.28 |
| 10-07 23:03 | +15 | ETH | UP | 0.51 | no | -5.28 |
| 10-07 23:03 | +10 | ETH | UP | 0.50 | no | -5.18 |
| 10-07 23:03 | +5 | ETH | UP | 0.50 | 0.59 | 0.55 |
| 10-07 23:02 | +10 stop | NEAR | UP | 0.64 | yes | 3.43 |
| 10-07 23:02 | +10 stop | HYPE | UP | 0.59 | yes | 3.93 |
| 10-07 23:02 | +20 | HYPE | UP | 0.59 | yes | 3.93 |
| 10-07 23:02 | +15 | HYPE | UP | 0.59 | yes | 3.93 |
| 10-07 23:02 | +10 | HYPE | UP | 0.59 | yes | 3.93 |
| 10-07 23:02 | +5 | HYPE | UP | 0.59 | yes | 3.93 |
| 10-07 23:01 | +10 stop | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-07 23:01 | +20 | DOGE | DOWN | 0.56 | no | 4.22 |
| 10-07 23:01 | +15 | DOGE | DOWN | 0.56 | no | 4.22 |
| 10-07 23:01 | +10 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-07 23:01 | +5 | DOGE | DOWN | 0.56 | 0.70 | 1.07 |
| 10-07 23:01 | +10 stop | NEAR | DOWN | 0.56 | 0.39 | -2.05 |
| 10-07 23:01 | +20 | NEAR | DOWN | 0.57 | yes | -5.87 |
| 10-07 23:01 | +15 | NEAR | DOWN | 0.57 | yes | -5.87 |
| 10-07 23:01 | +10 | NEAR | DOWN | 0.57 | yes | -5.87 |
| 10-07 23:01 | +5 | NEAR | DOWN | 0.57 | yes | -5.87 |
| 10-07 23:01 | +10 stop | SOL | UP | 0.63 | 0.76 | 0.99 |
| 10-07 23:01 | +20 | SOL | UP | 0.63 | yes | 3.52 |
| 10-07 23:01 | +15 | SOL | UP | 0.63 | yes | 3.52 |
| 10-07 23:01 | +10 | SOL | UP | 0.63 | 0.76 | 0.99 |
| 10-07 23:01 | +5 | SOL | UP | 0.63 | 0.71 | 0.47 |
| 10-07 23:01 | +10 stop | XRP | DOWN | 0.55 | no | 4.32 |
| 10-07 23:01 | +20 | XRP | DOWN | 0.55 | no | 4.32 |
| 10-07 23:01 | +15 | XRP | DOWN | 0.55 | no | 4.32 |
| 10-07 23:01 | +10 | XRP | DOWN | 0.55 | no | 4.32 |
| 10-07 23:01 | +5 | XRP | DOWN | 0.55 | no | 4.32 |
| 10-07 23:01 | +10 stop | BTC | DOWN | 0.60 | no | 3.83 |
| 10-07 23:01 | +20 | BTC | DOWN | 0.60 | no | 3.83 |
| 10-07 23:01 | +15 | BTC | DOWN | 0.60 | no | 3.83 |
| 10-07 23:01 | +10 | BTC | DOWN | 0.60 | no | 3.83 |
