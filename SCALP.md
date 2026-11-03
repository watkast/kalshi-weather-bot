# Range-Scalp Bot

*Updated Tue Nov 03 07:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45712 | 39805 | 5907 (69) | 2 | $-13173.61 | -4.6% |
| **+10¢** | 34124 | 27277 | 6847 (91) | 2 | $-12072.34 | -5.6% |
| **+15¢** | 28554 | 21188 | 7366 (119) | 2 | $-11060.95 | -6.2% |
| **+20¢** | 25361 | 17643 | 7718 (154) | 2 | $-9840.41 | -6.2% |
| **+10¢ (15¢ stop)** | 55778 | 55689 | 89 (53) | 0 | $-20995.42 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 07:12 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-03 07:12 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-03 07:12 | +10 stop | HYPE | DOWN | 0.63 | 0.84 | 1.83 |
| 11-03 07:12 | +10 | HYPE | DOWN | 0.62 | 0.84 | 1.91 |
| 11-03 07:12 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-03 07:12 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-03 07:10 | +10 stop | ETH | DOWN | 0.64 | 0.36 | -3.14 |
| 11-03 07:10 | +5 | ETH | DOWN | 0.64 | open |  |
| 11-03 07:10 | +10 stop | BNB | UP | 0.50 | 0.63 | 0.95 |
| 11-03 07:10 | +10 | BNB | UP | 0.51 | 0.63 | 0.85 |
| 11-03 07:09 | +10 stop | ETH | DOWN | 0.52 | 0.37 | -1.85 |
| 11-03 07:08 | +10 stop | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-03 07:08 | +5 | ETH | UP | 0.53 | 0.62 | 0.55 |
| 11-03 07:08 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 11-03 07:08 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-03 07:08 | +10 stop | NEAR | UP | 0.51 | 0.33 | -2.14 |
| 11-03 07:06 | +10 stop | ETH | DOWN | 0.51 | 0.64 | 0.95 |
| 11-03 07:06 | +10 stop | BNB | UP | 0.61 | 0.71 | 0.68 |
| 11-03 07:06 | +10 | BNB | UP | 0.61 | 0.71 | 0.68 |
| 11-03 07:05 | +10 stop | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-03 07:05 | +10 | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-03 07:05 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 11-03 07:05 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 11-03 07:05 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 11-03 07:05 | +5 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 07:04 | +5 | XRP | UP | 0.65 | 0.72 | 0.39 |
| 11-03 07:03 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 07:03 | +10 stop | XRP | UP | 0.63 | 0.77 | 1.10 |
| 11-03 07:03 | +10 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 11-03 07:03 | +5 | XRP | UP | 0.63 | 0.70 | 0.38 |
| 11-03 07:03 | +10 stop | BTC | DOWN | 0.69 | 0.51 | -2.13 |
| 11-03 07:03 | +10 stop | SOL | UP | 0.58 | 0.69 | 0.77 |
| 11-03 07:03 | +10 | SOL | UP | 0.58 | 0.69 | 0.77 |
| 11-03 07:03 | +5 | SOL | UP | 0.58 | 0.69 | 0.77 |
| 11-03 07:03 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.15 |
| 11-03 07:03 | +10 stop | ETH | UP | 0.54 | 0.33 | -2.44 |
| 11-03 07:03 | +10 | ETH | UP | 0.54 | 0.66 | 0.86 |
| 11-03 07:03 | +5 | ETH | UP | 0.54 | 0.62 | 0.45 |
| 11-03 07:03 | +10 stop | DOGE | UP | 0.57 | 0.41 | -1.95 |
| 11-03 07:02 | +5 | BNB | UP | 0.70 | 0.80 | 0.73 |
