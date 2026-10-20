# Range-Scalp Bot

*Updated Tue Oct 20 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25965 | 22608 | 3357 (32) | 0 | $-7615.12 | -4.7% |
| **+10¢** | 19546 | 15665 | 3881 (47) | 0 | $-6758.64 | -5.5% |
| **+15¢** | 16365 | 12190 | 4175 (71) | 0 | $-6031.67 | -5.9% |
| **+20¢** | 14478 | 10103 | 4375 (89) | 0 | $-5425.56 | -6.0% |
| **+10¢ (15¢ stop)** | 31861 | 31808 | 53 (30) | 0 | $-11749.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 17:39 | +10 stop | ZEC | DOWN | 0.57 | 0.70 | 0.97 |
| 10-20 17:38 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-20 17:38 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 10-20 17:37 | +10 stop | ETH | DOWN | 0.59 | 0.38 | -2.44 |
| 10-20 17:37 | +20 | ETH | DOWN | 0.59 | yes | -6.07 |
| 10-20 17:37 | +15 | ETH | DOWN | 0.59 | yes | -6.07 |
| 10-20 17:37 | +10 | ETH | DOWN | 0.60 | yes | -6.17 |
| 10-20 17:37 | +5 | ETH | DOWN | 0.60 | yes | -6.17 |
| 10-20 17:37 | +10 stop | ZEC | DOWN | 0.68 | 0.43 | -2.84 |
| 10-20 17:37 | +20 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-20 17:37 | +15 | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-20 17:37 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 17:37 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 17:37 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 10-20 17:37 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 10-20 17:37 | +10 stop | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-20 17:37 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.71 |
| 10-20 17:37 | +5 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 10-20 17:37 | +10 stop | BNB | DOWN | 0.63 | 0.43 | -2.35 |
| 10-20 17:37 | +15 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-20 17:37 | +10 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-20 17:37 | +5 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-20 17:37 | +5 | XRP | DOWN | 0.44 | 0.65 | 1.76 |
| 10-20 17:36 | +10 stop | NEAR | DOWN | 0.56 | 0.35 | -2.45 |
| 10-20 17:36 | +5 | BTC | DOWN | 0.68 | yes | -6.96 |
| 10-20 17:36 | +5 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 10-20 17:36 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 10-20 17:36 | +10 stop | DOGE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-20 17:35 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 10-20 17:34 | +10 stop | HYPE | DOWN | 0.50 | 0.34 | -1.94 |
| 10-20 17:34 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
| 10-20 17:34 | +10 stop | XRP | DOWN | 0.63 | 0.43 | -2.35 |
| 10-20 17:33 | +10 stop | HYPE | UP | 0.58 | 0.42 | -1.96 |
| 10-20 17:33 | +5 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-20 17:33 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 10-20 17:33 | +10 stop | DOGE | UP | 0.58 | 0.36 | -2.55 |
| 10-20 17:33 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-20 17:31 | +10 stop | SOL | DOWN | 0.54 | 0.38 | -1.95 |
| 10-20 17:31 | +20 | SOL | DOWN | 0.54 | yes | -5.58 |
| 10-20 17:31 | +15 | SOL | DOWN | 0.54 | yes | -5.58 |
