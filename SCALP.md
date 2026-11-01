# Range-Scalp Bot

*Updated Sun Nov 01 10:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43455 | 37870 | 5585 (63) | 2 | $-12390.33 | -4.5% |
| **+10¢** | 32419 | 25970 | 6449 (85) | 3 | $-11077.05 | -5.4% |
| **+15¢** | 27133 | 20188 | 6945 (112) | 5 | $-10101.96 | -5.9% |
| **+20¢** | 24095 | 16821 | 7274 (146) | 7 | $-8900.49 | -5.9% |
| **+10¢ (15¢ stop)** | 53010 | 52925 | 85 (50) | 1 | $-20031.78 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 10:06 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-01 10:05 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 11-01 10:05 | +5 | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-01 10:04 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.34 |
| 11-01 10:04 | +10 stop | ETH | DOWN | 0.54 | 0.71 | 1.37 |
| 11-01 10:04 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-01 10:04 | +10 stop | ETH | UP | 0.44 | 0.56 | 0.84 |
| 11-01 10:03 | +10 stop | XRP | UP | 0.70 | 0.49 | -2.43 |
| 11-01 10:03 | +10 stop | DOGE | UP | 0.71 | 0.48 | -2.63 |
| 11-01 10:03 | +10 stop | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 11-01 10:03 | +20 | BTC | DOWN | 0.58 | open |  |
| 11-01 10:03 | +15 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 11-01 10:03 | +10 | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 11-01 10:03 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-01 10:03 | +10 stop | HYPE | DOWN | 0.57 | 0.72 | 1.13 |
| 11-01 10:03 | +10 | HYPE | DOWN | 0.57 | 0.72 | 1.13 |
| 11-01 10:03 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-01 10:03 | +10 stop | ETH | DOWN | 0.65 | 0.41 | -2.71 |
| 11-01 10:03 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-01 10:03 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-01 10:03 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-01 10:03 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.31 |
| 11-01 10:03 | +10 stop | ZEC | DOWN | 0.68 | 0.47 | -2.44 |
| 11-01 10:03 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-01 10:03 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-01 10:03 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 10:03 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-01 10:03 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-01 10:02 | +10 stop | XRP | DOWN | 0.52 | 0.35 | -2.04 |
| 11-01 10:02 | +20 | XRP | DOWN | 0.52 | open |  |
| 11-01 10:02 | +15 | XRP | DOWN | 0.52 | open |  |
| 11-01 10:02 | +10 | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 11-01 10:02 | +5 | XRP | DOWN | 0.53 | 0.65 | 0.86 |
| 11-01 10:02 | +10 stop | DOGE | DOWN | 0.57 | 0.36 | -2.45 |
| 11-01 10:02 | +20 | DOGE | DOWN | 0.57 | open |  |
| 11-01 10:02 | +15 | DOGE | DOWN | 0.57 | open |  |
| 11-01 10:02 | +10 | DOGE | DOWN | 0.57 | open |  |
| 11-01 10:02 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.36 |
| 11-01 10:02 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.26 |
| 11-01 10:01 | +10 stop | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
