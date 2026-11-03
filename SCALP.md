# Range-Scalp Bot

*Updated Tue Nov 03 20:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46267 | 40286 | 5981 (72) | 0 | $-13315.18 | -4.6% |
| **+10¢** | 34538 | 27607 | 6931 (96) | 0 | $-12181.93 | -5.6% |
| **+15¢** | 28910 | 21456 | 7454 (124) | 0 | $-11132.51 | -6.1% |
| **+20¢** | 25682 | 17868 | 7814 (164) | 0 | $-9871.11 | -6.1% |
| **+10¢ (15¢ stop)** | 56440 | 56347 | 93 (56) | 0 | $-21178.99 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 19:55 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-03 19:55 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-03 19:55 | +20 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-03 19:55 | +15 | SOL | DOWN | 0.70 | yes | -7.15 |
| 11-03 19:55 | +10 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 19:55 | +5 | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 19:55 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-03 19:55 | +20 | XRP | DOWN | 0.65 | 0.91 | 2.41 |
| 11-03 19:55 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 11-03 19:55 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 19:55 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 19:55 | +10 stop | HYPE | UP | 0.59 | 0.43 | -1.95 |
| 11-03 19:55 | +20 | HYPE | UP | 0.59 | no | -6.11 |
| 11-03 19:55 | +15 | HYPE | UP | 0.59 | no | -6.11 |
| 11-03 19:55 | +10 | HYPE | UP | 0.61 | no | -6.27 |
| 11-03 19:55 | +5 | HYPE | UP | 0.60 | no | -6.21 |
| 11-03 19:54 | +10 stop | XRP | UP | 0.44 | 0.67 | 1.96 |
| 11-03 19:54 | +20 | XRP | UP | 0.44 | 0.67 | 1.96 |
| 11-03 19:54 | +15 | XRP | UP | 0.44 | 0.67 | 1.96 |
| 11-03 19:54 | +10 | XRP | UP | 0.41 | 0.67 | 2.22 |
| 11-03 19:54 | +5 | XRP | UP | 0.41 | 0.67 | 2.22 |
| 11-03 19:54 | +5 | NEAR | UP | 0.46 | 0.63 | 1.35 |
| 11-03 19:52 | +10 stop | ZEC | UP | 0.59 | 0.69 | 0.68 |
| 11-03 19:52 | +10 stop | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 11-03 19:52 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 11-03 19:51 | +10 stop | DOGE | UP | 0.63 | 0.45 | -2.15 |
| 11-03 19:51 | +5 | DOGE | UP | 0.63 | 0.68 | 0.17 |
| 11-03 19:51 | +10 stop | NEAR | DOWN | 0.47 | 0.71 | 2.07 |
| 11-03 19:51 | +10 stop | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 11-03 19:50 | +10 stop | BTC | UP | 0.56 | 0.41 | -1.85 |
| 11-03 19:50 | +15 | BTC | UP | 0.56 | 0.88 | 2.94 |
| 11-03 19:50 | +10 | BTC | UP | 0.56 | 0.88 | 2.94 |
| 11-03 19:50 | +5 | BTC | UP | 0.56 | 0.88 | 2.94 |
| 11-03 19:49 | +15 | SOL | UP | 0.69 | 0.84 | 1.25 |
| 11-03 19:48 | +10 stop | BNB | UP | 0.61 | 0.34 | -3.03 |
| 11-03 19:48 | +10 stop | ETH | UP | 0.57 | 0.40 | -2.05 |
| 11-03 19:48 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 11-03 19:48 | +10 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 11-03 19:48 | +5 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 11-03 19:48 | +10 | DOGE | UP | 0.61 | 0.71 | 0.68 |
