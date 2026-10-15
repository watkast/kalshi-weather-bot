# Range-Scalp Bot

*Updated Thu Oct 15 20:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18072 | 15688 | 2384 (28) | 5 | $-5545.62 | -4.9% |
| **+10¢** | 13647 | 10886 | 2761 (40) | 6 | $-5033.54 | -5.9% |
| **+15¢** | 11444 | 8474 | 2970 (59) | 7 | $-4551.71 | -6.3% |
| **+20¢** | 10171 | 7065 | 3106 (77) | 9 | $-3956.22 | -6.2% |
| **+10¢ (15¢ stop)** | 22239 | 22189 | 50 (29) | 2 | $-8612.37 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 20:05 | +10 stop | ETH | UP | 0.51 | 0.63 | 0.85 |
| 10-15 20:05 | +10 | ETH | UP | 0.51 | 0.63 | 0.85 |
| 10-15 20:05 | +5 | ETH | UP | 0.51 | 0.63 | 0.85 |
| 10-15 20:05 | +10 stop | BTC | UP | 0.49 | 0.66 | 1.36 |
| 10-15 20:05 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 10-15 20:05 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-15 20:05 | +20 | HYPE | UP | 0.62 | open |  |
| 10-15 20:05 | +15 | HYPE | UP | 0.62 | open |  |
| 10-15 20:05 | +10 | HYPE | UP | 0.64 | open |  |
| 10-15 20:05 | +5 | HYPE | UP | 0.64 | open |  |
| 10-15 20:05 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 10-15 20:05 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-15 20:05 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.29 |
| 10-15 20:05 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.04 |
| 10-15 20:05 | +5 | NEAR | DOWN | 0.67 | 0.80 | 1.04 |
| 10-15 20:04 | +10 stop | DOGE | UP | 0.67 | 0.37 | -3.33 |
| 10-15 20:04 | +10 stop | SOL | UP | 0.69 | 0.49 | -2.33 |
| 10-15 20:04 | +5 | XRP | DOWN | 0.70 | 0.78 | 0.52 |
| 10-15 20:04 | +10 stop | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-15 20:03 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 20:03 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-15 20:03 | +15 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 20:03 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-15 20:03 | +5 | XRP | DOWN | 0.62 | 0.69 | 0.38 |
| 10-15 20:03 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-15 20:03 | +20 | ETH | UP | 0.61 | open |  |
| 10-15 20:03 | +15 | ETH | UP | 0.61 | open |  |
| 10-15 20:03 | +10 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-15 20:03 | +5 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-15 20:03 | +10 stop | ZEC | DOWN | 0.56 | 0.39 | -2.05 |
| 10-15 20:03 | +20 | ZEC | DOWN | 0.56 | open |  |
| 10-15 20:03 | +15 | ZEC | DOWN | 0.56 | open |  |
| 10-15 20:03 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-15 20:03 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-15 20:02 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.05 |
| 10-15 20:02 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
| 10-15 20:02 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-15 20:02 | +15 | DOGE | DOWN | 0.63 | open |  |
| 10-15 20:02 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-15 20:02 | +5 | DOGE | DOWN | 0.63 | 0.69 | 0.28 |
