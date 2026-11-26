# Range-Scalp Bot

*Updated Thu Nov 26 11:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72619 | 63394 | 9225 (158) | 6 | $-19263.07 | -4.2% |
| **+10¢** | 54155 | 43382 | 10773 (203) | 7 | $-17845.28 | -5.2% |
| **+15¢** | 45347 | 33741 | 11606 (261) | 7 | $-15940.11 | -5.6% |
| **+20¢** | 40362 | 28141 | 12221 (327) | 8 | $-14327.08 | -5.7% |
| **+10¢ (15¢ stop)** | 88423 | 88214 | 209 (128) | 3 | $-32481.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 11:52 | +10 | HYPE | DOWN | 0.50 | open |  |
| 11-26 11:52 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-26 11:51 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-26 11:51 | +10 stop | ETH | DOWN | 0.43 | 0.59 | 1.25 |
| 11-26 11:51 | +10 stop | HYPE | DOWN | 0.67 | 0.51 | -1.94 |
| 11-26 11:51 | +10 stop | BTC | DOWN | 0.69 | 0.51 | -2.13 |
| 11-26 11:50 | +10 stop | NEAR | UP | 0.67 | 0.49 | -2.14 |
| 11-26 11:50 | +15 | NEAR | UP | 0.68 | open |  |
| 11-26 11:50 | +10 | NEAR | UP | 0.68 | open |  |
| 11-26 11:50 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-26 11:50 | +10 stop | XRP | DOWN | 0.62 | 0.80 | 1.46 |
| 11-26 11:49 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 11-26 11:49 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 11-26 11:49 | +10 stop | ZEC | UP | 0.50 | 0.18 | -3.49 |
| 11-26 11:49 | +10 stop | DOGE | UP | 0.51 | open |  |
| 11-26 11:48 | +5 | HYPE | DOWN | 0.68 | open |  |
| 11-26 11:48 | +10 stop | XRP | DOWN | 0.67 | 0.46 | -2.47 |
| 11-26 11:48 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-26 11:48 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.31 |
| 11-26 11:48 | +10 | XRP | DOWN | 0.67 | 0.80 | 0.99 |
| 11-26 11:48 | +5 | XRP | DOWN | 0.68 | 0.80 | 0.96 |
| 11-26 11:48 | +5 | NEAR | UP | 0.61 | 0.69 | 0.48 |
| 11-26 11:47 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-26 11:47 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-26 11:47 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-26 11:47 | +10 stop | ZEC | DOWN | 0.69 | 0.53 | -1.93 |
| 11-26 11:47 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-26 11:47 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-26 11:47 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-26 11:47 | +5 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-26 11:47 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-26 11:47 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-26 11:47 | +10 stop | SOL | DOWN | 0.53 | 0.33 | -2.34 |
| 11-26 11:47 | +20 | SOL | DOWN | 0.53 | open |  |
| 11-26 11:47 | +15 | SOL | DOWN | 0.53 | open |  |
| 11-26 11:47 | +10 | SOL | DOWN | 0.53 | open |  |
| 11-26 11:47 | +5 | SOL | DOWN | 0.53 | open |  |
| 11-26 11:46 | +10 stop | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 11-26 11:46 | +20 | NEAR | UP | 0.58 | open |  |
| 11-26 11:46 | +15 | NEAR | UP | 0.58 | 0.74 | 1.28 |
