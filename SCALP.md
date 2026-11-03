# Range-Scalp Bot

*Updated Tue Nov 03 08:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45760 | 39842 | 5918 (69) | 0 | $-13222.78 | -4.6% |
| **+10¢** | 34169 | 27311 | 6858 (91) | 0 | $-12106.31 | -5.6% |
| **+15¢** | 28588 | 21210 | 7378 (119) | 1 | $-11103.15 | -6.2% |
| **+20¢** | 25393 | 17663 | 7730 (154) | 1 | $-9879.80 | -6.2% |
| **+10¢ (15¢ stop)** | 55834 | 55745 | 89 (53) | 0 | $-20980.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 08:02 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 08:02 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-03 08:02 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-03 08:02 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 08:02 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-03 08:01 | +10 stop | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 08:01 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-03 08:01 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 08:01 | +10 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-03 08:01 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 08:01 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-03 08:01 | +20 | ETH | DOWN | 0.67 | 0.90 | 2.07 |
| 11-03 08:01 | +15 | ETH | DOWN | 0.66 | 0.90 | 2.14 |
| 11-03 08:01 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-03 08:01 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-03 08:01 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.05 |
| 11-03 08:01 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.78 |
| 11-03 08:01 | +15 | ZEC | DOWN | 0.67 | 0.87 | 1.79 |
| 11-03 08:01 | +10 | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-03 08:01 | +5 | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-03 08:01 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-03 08:01 | +20 | HYPE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-03 08:01 | +15 | HYPE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-03 08:01 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-03 08:01 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-03 07:55 | +10 | BTC | UP | 0.64 | 0.80 | 1.31 |
| 11-03 07:54 | +5 | SOL | UP | 0.68 | 0.79 | 0.82 |
| 11-03 07:54 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-03 07:54 | +5 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-03 07:53 | +10 stop | BTC | UP | 0.48 | 0.58 | 0.64 |
| 11-03 07:53 | +10 | BTC | UP | 0.49 | 0.62 | 0.95 |
| 11-03 07:53 | +5 | BTC | UP | 0.49 | 0.58 | 0.54 |
| 11-03 07:53 | +10 stop | SOL | UP | 0.61 | 0.79 | 1.51 |
| 11-03 07:53 | +10 | SOL | UP | 0.61 | 0.79 | 1.51 |
| 11-03 07:53 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 11-03 07:49 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 11-03 07:49 | +10 | HYPE | UP | 0.65 | 0.76 | 0.81 |
| 11-03 07:49 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 11-03 07:49 | +10 stop | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 11-03 07:49 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
