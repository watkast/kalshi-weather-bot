# Range-Scalp Bot

*Updated Wed Oct 21 22:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27794 | 24210 | 3584 (39) | 0 | $-8038.25 | -4.6% |
| **+10¢** | 20884 | 16750 | 4134 (55) | 0 | $-7048.72 | -5.4% |
| **+15¢** | 17493 | 13045 | 4448 (78) | 0 | $-6277.61 | -5.7% |
| **+20¢** | 15489 | 10827 | 4662 (98) | 0 | $-5610.57 | -5.8% |
| **+10¢ (15¢ stop)** | 34124 | 34065 | 59 (32) | 0 | $-12708.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 21:58 | +10 stop | ZEC | DOWN | 0.54 | 0.31 | -2.63 |
| 10-21 21:58 | +5 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 10-21 21:56 | +10 stop | NEAR | UP | 0.54 | 0.34 | -2.34 |
| 10-21 21:56 | +10 stop | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 10-21 21:56 | +20 | ETH | DOWN | 0.69 | 0.92 | 2.13 |
| 10-21 21:56 | +15 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 10-21 21:56 | +10 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 10-21 21:56 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-21 21:56 | +5 | NEAR | UP | 0.53 | 0.60 | 0.35 |
| 10-21 21:55 | +5 | NEAR | DOWN | 0.50 | 0.63 | 0.95 |
| 10-21 21:55 | +10 stop | ZEC | UP | 0.67 | 0.36 | -3.43 |
| 10-21 21:55 | +20 | ZEC | UP | 0.67 | 0.99 | 3.05 |
| 10-21 21:55 | +15 | ZEC | UP | 0.67 | 0.82 | 1.25 |
| 10-21 21:55 | +10 | ZEC | UP | 0.66 | 0.82 | 1.33 |
| 10-21 21:55 | +5 | ZEC | UP | 0.66 | 0.75 | 0.60 |
| 10-21 21:55 | +10 stop | NEAR | DOWN | 0.69 | 0.39 | -3.32 |
| 10-21 21:54 | +10 stop | SOL | DOWN | 0.45 | 0.69 | 2.07 |
| 10-21 21:54 | +10 stop | SOL | UP | 0.44 | 0.58 | 1.01 |
| 10-21 21:53 | +10 stop | DOGE | DOWN | 0.50 | 0.75 | 2.18 |
| 10-21 21:53 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.25 |
| 10-21 21:53 | +10 stop | HYPE | UP | 0.69 | 0.09 | -6.25 |
| 10-21 21:53 | +10 stop | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-21 21:52 | +5 | DOGE | UP | 0.67 | no | -6.86 |
| 10-21 21:52 | +10 stop | SOL | UP | 0.69 | 0.44 | -2.83 |
| 10-21 21:52 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 10-21 21:52 | +5 | HYPE | DOWN | 0.57 | 0.91 | 3.19 |
| 10-21 21:51 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.33 |
| 10-21 21:51 | +10 stop | HYPE | DOWN | 0.59 | 0.31 | -3.12 |
| 10-21 21:51 | +10 | HYPE | DOWN | 0.59 | 0.91 | 3.00 |
| 10-21 21:51 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-21 21:51 | +10 stop | SOL | UP | 0.67 | 0.46 | -2.44 |
| 10-21 21:51 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-21 21:50 | +10 stop | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 10-21 21:50 | +5 | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 10-21 21:50 | +10 stop | ETH | DOWN | 0.64 | 0.39 | -2.84 |
| 10-21 21:50 | +10 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-21 21:49 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-21 21:49 | +5 | BNB | UP | 0.70 | 0.81 | 0.80 |
| 10-21 21:49 | +10 stop | NEAR | UP | 0.68 | 0.47 | -2.44 |
| 10-21 21:48 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
