# Range-Scalp Bot

*Updated Thu Oct 15 09:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17271 | 14997 | 2274 (28) | 0 | $-5238.39 | -4.8% |
| **+10¢** | 13054 | 10417 | 2637 (40) | 0 | $-4762.57 | -5.8% |
| **+15¢** | 10965 | 8133 | 2832 (59) | 0 | $-4217.88 | -6.1% |
| **+20¢** | 9741 | 6776 | 2965 (77) | 0 | $-3674.95 | -6.0% |
| **+10¢ (15¢ stop)** | 21227 | 21177 | 50 (29) | 0 | $-8214.19 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 09:14 | +10 stop | SOL | DOWN | 0.52 | 0.10 | -4.44 |
| 10-15 09:14 | +15 | SOL | DOWN | 0.51 | yes | -5.26 |
| 10-15 09:13 | +10 | SOL | DOWN | 0.71 | yes | -7.25 |
| 10-15 09:13 | +10 stop | BTC | DOWN | 0.22 | 0.59 | 3.40 |
| 10-15 09:12 | +10 stop | BTC | UP | 0.54 | 0.38 | -1.95 |
| 10-15 09:12 | +5 | BTC | UP | 0.54 | 0.81 | 2.41 |
| 10-15 09:12 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-15 09:12 | +20 | BTC | UP | 0.57 | 0.81 | 2.11 |
| 10-15 09:12 | +15 | BTC | UP | 0.57 | 0.81 | 2.11 |
| 10-15 09:12 | +5 | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-15 09:11 | +10 stop | SOL | UP | 0.66 | 0.38 | -3.13 |
| 10-15 09:11 | +20 | SOL | UP | 0.66 | 0.88 | 1.96 |
| 10-15 09:11 | +5 | SOL | UP | 0.66 | 0.88 | 1.96 |
| 10-15 09:11 | +10 stop | DOGE | DOWN | 0.54 | 0.74 | 1.68 |
| 10-15 09:11 | +5 | DOGE | DOWN | 0.54 | 0.63 | 0.55 |
| 10-15 09:09 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-15 09:09 | +10 stop | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-15 09:09 | +20 | XRP | UP | 0.66 | 0.89 | 2.07 |
| 10-15 09:09 | +15 | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-15 09:09 | +10 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-15 09:08 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 09:08 | +10 stop | BNB | UP | 0.67 | 0.52 | -1.88 |
| 10-15 09:08 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-15 09:07 | +10 stop | XRP | UP | 0.55 | 0.69 | 1.07 |
| 10-15 09:07 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.21 |
| 10-15 09:07 | +20 | HYPE | UP | 0.65 | 0.86 | 1.84 |
| 10-15 09:07 | +15 | HYPE | UP | 0.65 | 0.86 | 1.84 |
| 10-15 09:06 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-15 09:06 | +5 | XRP | DOWN | 0.60 | yes | -6.17 |
| 10-15 09:06 | +10 stop | XRP | DOWN | 0.64 | 0.43 | -2.45 |
| 10-15 09:06 | +10 stop | BTC | DOWN | 0.66 | 0.44 | -2.54 |
| 10-15 09:05 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-15 09:05 | +15 | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 10-15 09:05 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.89 |
| 10-15 09:05 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-15 09:05 | +15 | ETH | UP | 0.63 | 0.79 | 1.31 |
| 10-15 09:05 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-15 09:05 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 10-15 09:05 | +10 stop | XRP | UP | 0.56 | 0.38 | -2.15 |
| 10-15 09:05 | +15 | XRP | UP | 0.56 | 0.79 | 2.00 |
