# Range-Scalp Bot

*Updated Mon Oct 26 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34240 | 29903 | 4337 (43) | 0 | $-9401.46 | -4.4% |
| **+10¢** | 25626 | 20606 | 5020 (65) | 0 | $-8257.48 | -5.1% |
| **+15¢** | 21427 | 16021 | 5406 (89) | 0 | $-7387.33 | -5.5% |
| **+20¢** | 18992 | 13331 | 5661 (111) | 1 | $-6463.29 | -5.4% |
| **+10¢ (15¢ stop)** | 41935 | 41873 | 62 (33) | 0 | $-15962.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 03:51 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 10-26 03:51 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-26 03:51 | +10 | HYPE | DOWN | 0.60 | 0.75 | 1.15 |
| 10-26 03:51 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.23 |
| 10-26 03:50 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 10-26 03:49 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-26 03:49 | +5 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 03:49 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-26 03:49 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 10-26 03:48 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-26 03:48 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.71 |
| 10-26 03:48 | +20 | DOGE | DOWN | 0.56 | 0.76 | 1.74 |
| 10-26 03:48 | +15 | DOGE | DOWN | 0.56 | 0.76 | 1.74 |
| 10-26 03:48 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.71 |
| 10-26 03:48 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.30 |
| 10-26 03:48 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-26 03:48 | +20 | NEAR | DOWN | 0.56 | 0.76 | 1.69 |
| 10-26 03:48 | +15 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-26 03:48 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 10-26 03:48 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.56 |
| 10-26 03:48 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-26 03:48 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-26 03:47 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 03:47 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-26 03:47 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-26 03:47 | +10 stop | ZEC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-26 03:47 | +20 | ZEC | DOWN | 0.54 | 0.81 | 2.41 |
| 10-26 03:47 | +15 | ZEC | DOWN | 0.54 | 0.71 | 1.37 |
| 10-26 03:47 | +10 | ZEC | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 03:47 | +5 | ZEC | DOWN | 0.53 | 0.62 | 0.55 |
| 10-26 03:46 | +10 stop | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 10-26 03:46 | +20 | HYPE | UP | 0.63 | open |  |
| 10-26 03:46 | +15 | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 10-26 03:46 | +10 | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 10-26 03:46 | +5 | HYPE | UP | 0.63 | 0.70 | 0.38 |
| 10-26 03:46 | +5 | BNB | DOWN | 0.65 | 0.78 | 0.97 |
| 10-26 03:46 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-26 03:46 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.02 |
| 10-26 03:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-26 03:46 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
