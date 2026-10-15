# Range-Scalp Bot

*Updated Thu Oct 15 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17057 | 14804 | 2253 (28) | 4 | $-5228.41 | -4.9% |
| **+10¢** | 12895 | 10283 | 2612 (40) | 3 | $-4752.63 | -5.9% |
| **+15¢** | 10826 | 8019 | 2807 (59) | 3 | $-4247.33 | -6.3% |
| **+20¢** | 9618 | 6679 | 2939 (76) | 4 | $-3726.89 | -6.2% |
| **+10¢ (15¢ stop)** | 20984 | 20934 | 50 (29) | 0 | $-8120.95 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 03:57 | +10 stop | DOGE | UP | 0.70 | 0.50 | -2.33 |
| 10-15 03:56 | +10 stop | NEAR | DOWN | 0.33 | 0.56 | 1.96 |
| 10-15 03:56 | +20 | NEAR | DOWN | 0.37 | open |  |
| 10-15 03:56 | +15 | NEAR | DOWN | 0.37 | 0.56 | 1.55 |
| 10-15 03:56 | +10 | NEAR | DOWN | 0.39 | 0.56 | 1.36 |
| 10-15 03:56 | +5 | NEAR | DOWN | 0.39 | 0.56 | 1.36 |
| 10-15 03:56 | +10 stop | ETH | UP | 0.64 | 0.86 | 1.94 |
| 10-15 03:56 | +10 stop | DOGE | DOWN | 0.70 | 0.46 | -2.73 |
| 10-15 03:56 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-15 03:56 | +10 stop | ETH | DOWN | 0.38 | 0.56 | 1.45 |
| 10-15 03:55 | +5 | BTC | UP | 0.59 | 0.78 | 1.60 |
| 10-15 03:55 | +10 stop | SOL | UP | 0.54 | 0.68 | 1.06 |
| 10-15 03:55 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 10-15 03:54 | +10 stop | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
| 10-15 03:54 | +20 | NEAR | DOWN | 0.58 | 0.82 | 2.11 |
| 10-15 03:54 | +15 | NEAR | DOWN | 0.58 | 0.76 | 1.49 |
| 10-15 03:54 | +10 | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
| 10-15 03:54 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 10-15 03:53 | +10 stop | DOGE | DOWN | 0.62 | 0.81 | 1.62 |
| 10-15 03:53 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-15 03:53 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-15 03:53 | +10 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-15 03:53 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-15 03:53 | +10 stop | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-15 03:53 | +15 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-15 03:53 | +10 | XRP | UP | 0.67 | 0.83 | 1.34 |
| 10-15 03:53 | +5 | XRP | UP | 0.67 | 0.73 | 0.30 |
| 10-15 03:53 | +10 stop | ETH | UP | 0.62 | 0.38 | -2.74 |
| 10-15 03:53 | +10 | ETH | UP | 0.63 | 0.86 | 2.04 |
| 10-15 03:53 | +5 | ETH | UP | 0.63 | 0.86 | 2.04 |
| 10-15 03:52 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-15 03:52 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-15 03:52 | +10 stop | XRP | UP | 0.66 | 0.80 | 1.12 |
| 10-15 03:52 | +10 stop | DOGE | DOWN | 0.64 | 0.46 | -2.15 |
| 10-15 03:52 | +5 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 03:51 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-15 03:51 | +5 | HYPE | UP | 0.64 | 0.72 | 0.48 |
| 10-15 03:50 | +10 stop | NEAR | UP | 0.58 | 0.72 | 1.07 |
| 10-15 03:50 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 10-15 03:50 | +10 stop | ETH | DOWN | 0.56 | 0.41 | -1.85 |
