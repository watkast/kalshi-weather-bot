# Range-Scalp Bot

*Updated Wed Oct 28 09:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37868 | 33044 | 4824 (46) | 0 | $-10637.98 | -4.5% |
| **+10¢** | 28267 | 22683 | 5584 (68) | 0 | $-9512.55 | -5.3% |
| **+15¢** | 23642 | 17646 | 5996 (93) | 0 | $-8477.34 | -5.7% |
| **+20¢** | 20966 | 14688 | 6278 (118) | 0 | $-7448.56 | -5.7% |
| **+10¢ (15¢ stop)** | 46385 | 46318 | 67 (35) | 0 | $-17658.49 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 09:27 | +10 stop | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 10-28 09:27 | +10 | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 10-28 09:27 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 10-28 09:27 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 10-28 09:27 | +5 | BNB | UP | 0.68 | 0.79 | 0.82 |
| 10-28 09:27 | +10 stop | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 10-28 09:27 | +5 | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 10-28 09:27 | +10 stop | ZEC | DOWN | 0.66 | 0.36 | -3.33 |
| 10-28 09:27 | +10 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 10-28 09:27 | +5 | ZEC | DOWN | 0.66 | yes | -6.76 |
| 10-28 09:26 | +10 stop | HYPE | UP | 0.59 | 0.77 | 1.54 |
| 10-28 09:26 | +15 | HYPE | UP | 0.59 | 0.77 | 1.54 |
| 10-28 09:26 | +10 | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-28 09:26 | +5 | HYPE | UP | 0.55 | 0.64 | 0.55 |
| 10-28 09:26 | +10 stop | ZEC | UP | 0.44 | 0.55 | 0.76 |
| 10-28 09:26 | +10 | ZEC | UP | 0.44 | 0.55 | 0.76 |
| 10-28 09:26 | +5 | ZEC | UP | 0.44 | 0.55 | 0.76 |
| 10-28 09:25 | +10 stop | SOL | UP | 0.62 | 0.29 | -3.62 |
| 10-28 09:25 | +10 stop | HYPE | UP | 0.49 | 0.66 | 1.31 |
| 10-28 09:25 | +20 | HYPE | UP | 0.49 | 0.77 | 2.44 |
| 10-28 09:25 | +15 | HYPE | UP | 0.50 | 0.66 | 1.29 |
| 10-28 09:25 | +10 | HYPE | UP | 0.49 | 0.66 | 1.37 |
| 10-28 09:25 | +5 | HYPE | UP | 0.49 | 0.56 | 0.35 |
| 10-28 09:24 | +10 stop | ETH | DOWN | 0.59 | 0.83 | 2.13 |
| 10-28 09:24 | +20 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-28 09:24 | +15 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-28 09:24 | +10 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-28 09:24 | +5 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-28 09:24 | +10 stop | BNB | UP | 0.55 | 0.66 | 0.76 |
| 10-28 09:24 | +5 | BNB | UP | 0.55 | 0.60 | 0.15 |
| 10-28 09:24 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-28 09:24 | +5 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-28 09:24 | +10 stop | DOGE | UP | 0.54 | 0.80 | 2.30 |
| 10-28 09:24 | +10 stop | SOL | DOWN | 0.61 | 0.30 | -3.42 |
| 10-28 09:24 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 10-28 09:24 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-28 09:23 | +10 stop | BNB | UP | 0.67 | 0.81 | 1.13 |
| 10-28 09:23 | +5 | BNB | UP | 0.67 | 0.74 | 0.40 |
| 10-28 09:23 | +10 stop | DOGE | DOWN | 0.61 | 0.41 | -2.34 |
| 10-28 09:23 | +10 stop | ZEC | UP | 0.59 | 0.70 | 0.78 |
