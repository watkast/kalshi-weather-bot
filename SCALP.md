# Range-Scalp Bot

*Updated Tue Oct 27 12:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36562 | 31926 | 4636 (43) | 5 | $-10123.62 | -4.4% |
| **+10¢** | 27316 | 21955 | 5361 (65) | 4 | $-8933.81 | -5.2% |
| **+15¢** | 22853 | 17100 | 5753 (89) | 4 | $-7857.53 | -5.5% |
| **+20¢** | 20251 | 14225 | 6026 (113) | 5 | $-6875.52 | -5.4% |
| **+10¢ (15¢ stop)** | 44814 | 44751 | 63 (33) | 3 | $-17090.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 12:49 | +10 stop | NEAR | UP | 0.67 | open |  |
| 10-27 12:49 | +20 | NEAR | UP | 0.67 | open |  |
| 10-27 12:49 | +15 | NEAR | UP | 0.67 | open |  |
| 10-27 12:49 | +10 | NEAR | UP | 0.67 | open |  |
| 10-27 12:49 | +5 | NEAR | UP | 0.67 | open |  |
| 10-27 12:49 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-27 12:49 | +10 | HYPE | UP | 0.64 | open |  |
| 10-27 12:49 | +5 | HYPE | UP | 0.64 | open |  |
| 10-27 12:49 | +10 stop | ZEC | UP | 0.53 | open |  |
| 10-27 12:48 | +5 | BTC | UP | 0.70 | open |  |
| 10-27 12:48 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-27 12:47 | +5 | SOL | DOWN | 0.55 | open |  |
| 10-27 12:46 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-27 12:46 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 10-27 12:46 | +10 stop | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-27 12:46 | +20 | BTC | UP | 0.56 | open |  |
| 10-27 12:46 | +15 | BTC | UP | 0.56 | 0.74 | 1.48 |
| 10-27 12:46 | +10 | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-27 12:46 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-27 12:46 | +10 stop | SOL | DOWN | 0.58 | 0.35 | -2.64 |
| 10-27 12:46 | +20 | SOL | DOWN | 0.58 | open |  |
| 10-27 12:46 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-27 12:46 | +10 | SOL | DOWN | 0.57 | open |  |
| 10-27 12:46 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 10-27 12:46 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-27 12:46 | +20 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-27 12:46 | +15 | ETH | UP | 0.57 | 0.75 | 1.48 |
| 10-27 12:46 | +10 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-27 12:46 | +5 | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-27 12:46 | +10 stop | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-27 12:46 | +20 | BNB | UP | 0.55 | 0.75 | 1.68 |
| 10-27 12:46 | +15 | BNB | UP | 0.55 | 0.70 | 1.17 |
| 10-27 12:46 | +10 | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-27 12:46 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 10-27 12:46 | +10 stop | HYPE | UP | 0.53 | 0.65 | 0.82 |
| 10-27 12:46 | +20 | HYPE | UP | 0.54 | open |  |
| 10-27 12:46 | +15 | HYPE | UP | 0.54 | open |  |
| 10-27 12:46 | +10 | HYPE | UP | 0.54 | 0.65 | 0.76 |
| 10-27 12:46 | +5 | HYPE | UP | 0.54 | 0.65 | 0.76 |
| 10-27 12:46 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
