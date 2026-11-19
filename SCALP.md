# Range-Scalp Bot

*Updated Thu Nov 19 15:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65121 | 56842 | 8279 (124) | 3 | $-17457.39 | -4.3% |
| **+10¢** | 48634 | 38950 | 9684 (165) | 4 | $-16243.67 | -5.3% |
| **+15¢** | 40776 | 30329 | 10447 (210) | 7 | $-14663.82 | -5.7% |
| **+20¢** | 36317 | 25345 | 10972 (265) | 6 | $-12955.53 | -5.7% |
| **+10¢ (15¢ stop)** | 79255 | 79091 | 164 (98) | 0 | $-29126.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 15:58 | +10 stop | SOL | DOWN | 0.56 | 0.86 | 2.73 |
| 11-19 15:58 | +5 | SOL | DOWN | 0.61 | 0.86 | 2.24 |
| 11-19 15:58 | +10 stop | HYPE | UP | 0.71 | 0.51 | -2.33 |
| 11-19 15:58 | +20 | HYPE | UP | 0.71 | open |  |
| 11-19 15:58 | +15 | HYPE | UP | 0.71 | open |  |
| 11-19 15:58 | +10 stop | ZEC | DOWN | 0.53 | 0.83 | 2.72 |
| 11-19 15:58 | +20 | ZEC | DOWN | 0.54 | 0.83 | 2.63 |
| 11-19 15:58 | +5 | ZEC | DOWN | 0.55 | 0.83 | 2.52 |
| 11-19 15:57 | +10 stop | NEAR | DOWN | 0.50 | 0.63 | 0.95 |
| 11-19 15:57 | +20 | NEAR | DOWN | 0.50 | 0.88 | 3.54 |
| 11-19 15:57 | +15 | NEAR | DOWN | 0.50 | 0.88 | 3.54 |
| 11-19 15:57 | +10 | NEAR | DOWN | 0.50 | 0.63 | 0.95 |
| 11-19 15:57 | +5 | NEAR | DOWN | 0.53 | 0.63 | 0.65 |
| 11-19 15:56 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-19 15:56 | +5 | SOL | UP | 0.58 | 0.68 | 0.66 |
| 11-19 15:56 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 11-19 15:55 | +5 | ETH | UP | 0.39 | 0.55 | 1.25 |
| 11-19 15:55 | +10 stop | ETH | UP | 0.60 | 0.36 | -2.74 |
| 11-19 15:55 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-19 15:54 | +10 stop | HYPE | DOWN | 0.68 | 0.82 | 1.10 |
| 11-19 15:54 | +15 | HYPE | DOWN | 0.68 | 0.88 | 1.73 |
| 11-19 15:54 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-19 15:54 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-19 15:54 | +10 stop | ZEC | DOWN | 0.71 | 0.51 | -2.33 |
| 11-19 15:54 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-19 15:54 | +5 | ZEC | DOWN | 0.71 | 0.80 | 0.63 |
| 11-19 15:54 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-19 15:54 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-19 15:54 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-19 15:54 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-19 15:54 | +5 | XRP | DOWN | 0.62 | 0.71 | 0.58 |
| 11-19 15:53 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-19 15:53 | +10 stop | BNB | DOWN | 0.52 | 0.34 | -2.14 |
| 11-19 15:53 | +10 stop | ETH | DOWN | 0.57 | 0.42 | -1.86 |
| 11-19 15:53 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-19 15:53 | +5 | ETH | DOWN | 0.58 | 0.66 | 0.46 |
| 11-19 15:53 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 11-19 15:52 | +10 stop | DOGE | DOWN | 0.69 | 0.46 | -2.63 |
| 11-19 15:51 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 11-19 15:51 | +5 | SOL | DOWN | 0.66 | 0.74 | 0.50 |
