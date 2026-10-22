# Range-Scalp Bot

*Updated Thu Oct 22 02:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28101 | 24487 | 3614 (39) | 2 | $-8066.47 | -4.6% |
| **+10¢** | 21114 | 16937 | 4177 (55) | 2 | $-7116.47 | -5.4% |
| **+15¢** | 17688 | 13195 | 4493 (78) | 2 | $-6327.18 | -5.7% |
| **+20¢** | 15655 | 10945 | 4710 (98) | 2 | $-5673.46 | -5.8% |
| **+10¢ (15¢ stop)** | 34503 | 34444 | 59 (32) | 0 | $-12892.49 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 02:18 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 02:18 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 02:18 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-22 02:17 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-22 02:17 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-22 02:17 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 1.00 |
| 10-22 02:17 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.84 |
| 10-22 02:17 | +15 | HYPE | DOWN | 0.69 | 0.88 | 1.63 |
| 10-22 02:17 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.00 |
| 10-22 02:17 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.48 |
| 10-22 02:17 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-22 02:17 | +20 | ZEC | DOWN | 0.62 | 0.89 | 2.46 |
| 10-22 02:17 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-22 02:17 | +10 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-22 02:17 | +5 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-22 02:17 | +10 stop | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 10-22 02:17 | +20 | NEAR | DOWN | 0.60 | 0.84 | 2.13 |
| 10-22 02:17 | +15 | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 10-22 02:17 | +10 | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 10-22 02:17 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 10-22 02:17 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 02:17 | +20 | SOL | DOWN | 0.68 | 0.93 | 2.30 |
| 10-22 02:17 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-22 02:17 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 02:17 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-22 02:17 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-22 02:16 | +10 stop | BTC | UP | 0.64 | 0.42 | -2.55 |
| 10-22 02:16 | +20 | BTC | UP | 0.64 | open |  |
| 10-22 02:16 | +15 | BTC | UP | 0.64 | open |  |
| 10-22 02:16 | +10 | BTC | UP | 0.64 | open |  |
| 10-22 02:16 | +5 | BTC | UP | 0.64 | open |  |
| 10-22 02:16 | +10 stop | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-22 02:16 | +20 | DOGE | DOWN | 0.57 | 0.80 | 2.00 |
| 10-22 02:16 | +15 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-22 02:16 | +10 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-22 02:16 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-22 02:16 | +10 stop | ETH | UP | 0.65 | 0.38 | -3.03 |
| 10-22 02:16 | +20 | ETH | UP | 0.65 | open |  |
| 10-22 02:16 | +15 | ETH | UP | 0.65 | open |  |
| 10-22 02:16 | +10 | ETH | UP | 0.65 | open |  |
