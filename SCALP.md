# Range-Scalp Bot

*Updated Sun Nov 01 07:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43316 | 37753 | 5563 (63) | 1 | $-12333.14 | -4.5% |
| **+10¢** | 32303 | 25878 | 6425 (85) | 1 | $-11032.52 | -5.4% |
| **+15¢** | 27031 | 20108 | 6923 (112) | 1 | $-10098.47 | -6.0% |
| **+20¢** | 24007 | 16755 | 7252 (146) | 1 | $-8905.73 | -5.9% |
| **+10¢ (15¢ stop)** | 52801 | 52716 | 85 (50) | 0 | $-19936.26 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 07:22 | +10 stop | NEAR | DOWN | 0.57 | 0.37 | -2.35 |
| 11-01 07:20 | +10 stop | NEAR | DOWN | 0.65 | 0.38 | -3.03 |
| 11-01 07:20 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-01 07:20 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-01 07:20 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-01 07:20 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-01 07:16 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-01 07:16 | +20 | HYPE | DOWN | 0.69 | 0.93 | 2.23 |
| 11-01 07:16 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 07:16 | +10 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-01 07:16 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-01 07:11 | +10 stop | XRP | UP | 0.49 | 0.72 | 1.97 |
| 11-01 07:09 | +10 stop | HYPE | UP | 0.56 | 0.35 | -2.40 |
| 11-01 07:09 | +5 | HYPE | UP | 0.56 | no | -5.74 |
| 11-01 07:07 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 11-01 07:07 | +5 | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 11-01 07:06 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 11-01 07:06 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 07:06 | +10 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-01 07:06 | +5 | DOGE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-01 07:06 | +10 stop | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-01 07:06 | +10 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-01 07:06 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 11-01 07:05 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-01 07:05 | +5 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-01 07:05 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
| 11-01 07:04 | +10 stop | ZEC | UP | 0.62 | 0.44 | -2.15 |
| 11-01 07:04 | +10 stop | XRP | UP | 0.52 | 0.62 | 0.65 |
| 11-01 07:04 | +10 stop | NEAR | UP | 0.59 | 0.32 | -3.03 |
| 11-01 07:03 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 07:03 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.06 |
| 11-01 07:03 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-01 07:03 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 07:03 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 07:03 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-01 07:03 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 07:03 | +20 | SOL | DOWN | 0.64 | 0.91 | 2.45 |
| 11-01 07:03 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 11-01 07:03 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-01 07:03 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
