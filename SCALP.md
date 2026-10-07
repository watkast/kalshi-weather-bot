# Range-Scalp Bot

*Updated Wed Oct 07 08:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6187 | 5370 | 817 (9) | 0 | $-1862.90 | -4.8% |
| **+10¢** | 4716 | 3756 | 960 (16) | 0 | $-1735.94 | -5.8% |
| **+15¢** | 3960 | 2944 | 1016 (20) | 0 | $-1474.15 | -5.9% |
| **+20¢** | 3542 | 2481 | 1061 (27) | 0 | $-1194.91 | -5.4% |
| **+10¢ (15¢ stop)** | 7498 | 7483 | 15 (9) | 0 | $-2600.39 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 08:09 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-07 08:09 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-07 08:08 | +10 stop | SOL | UP | 0.46 | 0.58 | 0.84 |
| 10-07 08:08 | +10 stop | HYPE | UP | 0.66 | 0.48 | -2.14 |
| 10-07 08:08 | +10 stop | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 10-07 08:07 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 10-07 08:07 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-07 08:07 | +10 stop | SOL | DOWN | 0.69 | 0.50 | -2.23 |
| 10-07 08:07 | +10 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 08:07 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-07 08:06 | +10 stop | HYPE | UP | 0.68 | 0.50 | -2.14 |
| 10-07 08:06 | +10 | HYPE | UP | 0.68 | 0.86 | 1.55 |
| 10-07 08:06 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 10-07 08:06 | +10 stop | NEAR | UP | 0.67 | 0.51 | -1.94 |
| 10-07 08:06 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-07 08:05 | +10 stop | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-07 08:05 | +5 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 10-07 08:04 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-07 08:04 | +10 stop | ZEC | UP | 0.58 | 0.34 | -2.74 |
| 10-07 08:04 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 10-07 08:04 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-07 08:04 | +20 | BTC | DOWN | 0.63 | 0.89 | 2.36 |
| 10-07 08:04 | +15 | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-07 08:04 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-07 08:04 | +5 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-07 08:04 | +10 stop | SOL | UP | 0.58 | 0.37 | -2.44 |
| 10-07 08:04 | +10 stop | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-07 08:04 | +5 | SOL | UP | 0.58 | 0.64 | 0.26 |
| 10-07 08:03 | +5 | XRP | DOWN | 0.50 | 0.55 | 0.14 |
| 10-07 08:03 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 10-07 08:03 | +5 | SOL | DOWN | 0.60 | 0.66 | 0.27 |
| 10-07 08:03 | +10 stop | NEAR | DOWN | 0.56 | 0.40 | -1.95 |
| 10-07 08:03 | +20 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 10-07 08:03 | +15 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 10-07 08:03 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-07 08:03 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 10-07 08:02 | +10 stop | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-07 08:02 | +10 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 10-07 08:02 | +5 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 10-07 08:02 | +5 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
