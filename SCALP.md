# Range-Scalp Bot

*Updated Thu Oct 22 13:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28789 | 25087 | 3702 (39) | 7 | $-8276.42 | -4.6% |
| **+10¢** | 21608 | 17326 | 4282 (55) | 7 | $-7353.63 | -5.4% |
| **+15¢** | 18083 | 13479 | 4604 (78) | 8 | $-6568.06 | -5.8% |
| **+20¢** | 16000 | 11171 | 4829 (100) | 8 | $-5920.05 | -5.9% |
| **+10¢ (15¢ stop)** | 35317 | 35258 | 59 (32) | 2 | $-13240.52 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 13:38 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 10-22 13:38 | +10 stop | ZEC | UP | 0.66 | open |  |
| 10-22 13:38 | +20 | ZEC | UP | 0.69 | open |  |
| 10-22 13:38 | +15 | ZEC | UP | 0.69 | open |  |
| 10-22 13:38 | +10 | ZEC | UP | 0.69 | open |  |
| 10-22 13:38 | +5 | ZEC | UP | 0.69 | open |  |
| 10-22 13:38 | +10 stop | DOGE | UP | 0.66 | 0.45 | -2.44 |
| 10-22 13:38 | +15 | DOGE | UP | 0.67 | open |  |
| 10-22 13:38 | +10 | DOGE | UP | 0.68 | open |  |
| 10-22 13:38 | +5 | DOGE | UP | 0.68 | open |  |
| 10-22 13:38 | +10 stop | ETH | UP | 0.56 | 0.39 | -2.05 |
| 10-22 13:38 | +5 | NEAR | UP | 0.64 | open |  |
| 10-22 13:37 | +10 stop | NEAR | UP | 0.59 | open |  |
| 10-22 13:37 | +20 | NEAR | UP | 0.59 | open |  |
| 10-22 13:37 | +15 | NEAR | UP | 0.59 | open |  |
| 10-22 13:37 | +10 | NEAR | UP | 0.56 | open |  |
| 10-22 13:37 | +5 | NEAR | UP | 0.56 | 0.62 | 0.25 |
| 10-22 13:37 | +10 stop | BNB | UP | 0.69 | 0.41 | -3.12 |
| 10-22 13:36 | +10 stop | BNB | UP | 0.54 | 0.68 | 1.06 |
| 10-22 13:34 | +10 stop | BTC | UP | 0.59 | 0.71 | 0.88 |
| 10-22 13:34 | +10 stop | ETH | UP | 0.71 | 0.87 | 1.37 |
| 10-22 13:33 | +10 stop | BNB | UP | 0.57 | 0.72 | 1.17 |
| 10-22 13:33 | +10 stop | HYPE | UP | 0.71 | 0.56 | -1.83 |
| 10-22 13:33 | +10 stop | ETH | UP | 0.50 | 0.62 | 0.85 |
| 10-22 13:33 | +10 stop | XRP | UP | 0.60 | 0.72 | 0.88 |
| 10-22 13:33 | +10 stop | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-22 13:33 | +20 | DOGE | UP | 0.71 | open |  |
| 10-22 13:33 | +15 | DOGE | UP | 0.71 | 0.91 | 1.77 |
| 10-22 13:33 | +10 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-22 13:33 | +5 | DOGE | UP | 0.71 | 0.84 | 1.05 |
| 10-22 13:32 | +10 stop | BTC | DOWN | 0.60 | 0.44 | -1.95 |
| 10-22 13:32 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-22 13:32 | +15 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 10-22 13:32 | +10 | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-22 13:32 | +5 | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-22 13:32 | +10 stop | SOL | DOWN | 0.56 | 0.41 | -1.85 |
| 10-22 13:32 | +20 | SOL | DOWN | 0.56 | open |  |
| 10-22 13:32 | +15 | SOL | DOWN | 0.56 | open |  |
| 10-22 13:32 | +10 | SOL | DOWN | 0.56 | open |  |
| 10-22 13:32 | +5 | SOL | DOWN | 0.56 | open |  |
