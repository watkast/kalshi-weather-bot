# Range-Scalp Bot

*Updated Wed Nov 04 09:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47044 | 40967 | 6077 (72) | 0 | $-13543.92 | -4.6% |
| **+10¢** | 35143 | 28094 | 7049 (97) | 0 | $-12369.20 | -5.6% |
| **+15¢** | 29431 | 21842 | 7589 (125) | 0 | $-11336.40 | -6.1% |
| **+20¢** | 26145 | 18195 | 7950 (165) | 1 | $-10008.71 | -6.1% |
| **+10¢ (15¢ stop)** | 57327 | 57234 | 93 (56) | 0 | $-21360.88 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 09:31 | +10 stop | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +20 | SOL | UP | 0.66 | 0.91 | 2.31 |
| 11-04 09:31 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +10 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +5 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-04 09:31 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +20 | ZEC | UP | 0.65 | open |  |
| 11-04 09:31 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +10 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-04 09:31 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 11-04 09:30 | +10 stop | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +20 | HYPE | UP | 0.62 | 0.85 | 2.04 |
| 11-04 09:30 | +15 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +10 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-04 09:30 | +5 | HYPE | UP | 0.62 | 0.69 | 0.38 |
| 11-04 09:18 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 09:18 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 11-04 09:18 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-04 09:18 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-04 09:17 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:17 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:17 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-04 09:17 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-04 09:17 | +10 stop | NEAR | UP | 0.53 | 0.31 | -2.53 |
| 11-04 09:17 | +20 | NEAR | UP | 0.53 | no | -5.48 |
| 11-04 09:17 | +15 | NEAR | UP | 0.53 | no | -5.48 |
| 11-04 09:17 | +10 | NEAR | UP | 0.53 | no | -5.48 |
| 11-04 09:17 | +5 | NEAR | UP | 0.53 | 0.59 | 0.25 |
| 11-04 09:16 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 09:16 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-04 09:16 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 09:16 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 09:16 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-04 09:16 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 09:16 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-04 09:16 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:16 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:16 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-04 09:16 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-04 09:16 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
