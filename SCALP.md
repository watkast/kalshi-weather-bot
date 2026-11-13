# Range-Scalp Bot

*Updated Fri Nov 13 11:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58225 | 50804 | 7421 (102) | 0 | $-15727.15 | -4.3% |
| **+10¢** | 43504 | 34827 | 8677 (134) | 0 | $-14694.39 | -5.4% |
| **+15¢** | 36475 | 27132 | 9343 (169) | 0 | $-13249.91 | -5.8% |
| **+20¢** | 32499 | 22688 | 9811 (220) | 0 | $-11633.56 | -5.7% |
| **+10¢ (15¢ stop)** | 70940 | 70811 | 129 (79) | 0 | $-26081.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 11:40 | +10 stop | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-13 11:40 | +15 | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-13 11:40 | +10 | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-13 11:40 | +5 | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-13 11:40 | +10 stop | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 11-13 11:40 | +20 | BTC | DOWN | 0.47 | yes | -4.88 |
| 11-13 11:40 | +15 | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 11-13 11:40 | +10 | BTC | DOWN | 0.47 | 0.64 | 1.35 |
| 11-13 11:40 | +5 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 11-13 11:38 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-13 11:37 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.12 |
| 11-13 11:37 | +10 stop | DOGE | DOWN | 0.54 | 0.36 | -2.15 |
| 11-13 11:36 | +5 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 11-13 11:36 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
| 11-13 11:34 | +10 stop | SOL | DOWN | 0.71 | 0.48 | -2.63 |
| 11-13 11:34 | +15 | SOL | DOWN | 0.71 | yes | -7.25 |
| 11-13 11:34 | +10 | SOL | DOWN | 0.71 | yes | -7.25 |
| 11-13 11:34 | +5 | SOL | DOWN | 0.71 | yes | -7.25 |
| 11-13 11:33 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 11-13 11:33 | +5 | ETH | DOWN | 0.59 | yes | -6.11 |
| 11-13 11:32 | +10 stop | XRP | DOWN | 0.67 | 0.39 | -3.13 |
| 11-13 11:32 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 11-13 11:32 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-13 11:31 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.11 |
| 11-13 11:31 | +20 | HYPE | DOWN | 0.68 | yes | -6.93 |
| 11-13 11:31 | +15 | HYPE | DOWN | 0.68 | yes | -6.93 |
| 11-13 11:31 | +10 | HYPE | DOWN | 0.68 | yes | -6.93 |
| 11-13 11:31 | +5 | HYPE | DOWN | 0.68 | yes | -6.93 |
| 11-13 11:31 | +10 stop | ETH | DOWN | 0.58 | 0.39 | -2.25 |
| 11-13 11:31 | +20 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-13 11:31 | +15 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-13 11:31 | +10 | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-13 11:31 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-13 11:31 | +10 stop | ZEC | DOWN | 0.67 | 0.48 | -2.24 |
| 11-13 11:31 | +20 | ZEC | DOWN | 0.67 | yes | -6.86 |
| 11-13 11:31 | +15 | ZEC | DOWN | 0.67 | yes | -6.86 |
| 11-13 11:31 | +10 | ZEC | DOWN | 0.67 | yes | -6.86 |
| 11-13 11:31 | +5 | ZEC | DOWN | 0.67 | yes | -6.86 |
| 11-13 11:31 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-13 11:31 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
