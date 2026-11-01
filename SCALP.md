# Range-Scalp Bot

*Updated Sun Nov 01 21:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44003 | 38332 | 5671 (65) | 4 | $-12629.77 | -4.6% |
| **+10¢** | 32833 | 26282 | 6551 (86) | 5 | $-11359.76 | -5.5% |
| **+15¢** | 27474 | 20423 | 7051 (113) | 5 | $-10376.33 | -6.0% |
| **+20¢** | 24402 | 17018 | 7384 (147) | 5 | $-9141.09 | -6.0% |
| **+10¢ (15¢ stop)** | 53674 | 53588 | 86 (51) | 0 | $-20317.61 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 21:51 | +10 stop | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-01 21:51 | +5 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-01 21:50 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 11-01 21:49 | +10 stop | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-01 21:49 | +10 stop | HYPE | UP | 0.66 | 0.49 | -2.08 |
| 11-01 21:49 | +10 | HYPE | UP | 0.66 | open |  |
| 11-01 21:49 | +10 stop | XRP | UP | 0.55 | 0.32 | -2.64 |
| 11-01 21:49 | +10 | XRP | UP | 0.55 | open |  |
| 11-01 21:49 | +5 | XRP | UP | 0.55 | open |  |
| 11-01 21:49 | +10 stop | ETH | UP | 0.59 | 0.24 | -3.80 |
| 11-01 21:49 | +15 | ETH | UP | 0.59 | open |  |
| 11-01 21:49 | +10 | ETH | UP | 0.59 | open |  |
| 11-01 21:49 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 11-01 21:48 | +5 | HYPE | UP | 0.69 | open |  |
| 11-01 21:48 | +10 stop | BTC | UP | 0.59 | 0.36 | -2.64 |
| 11-01 21:48 | +10 | BTC | UP | 0.59 | open |  |
| 11-01 21:48 | +5 | BTC | UP | 0.59 | open |  |
| 11-01 21:48 | +10 stop | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-01 21:48 | +20 | HYPE | UP | 0.62 | open |  |
| 11-01 21:48 | +15 | HYPE | UP | 0.62 | open |  |
| 11-01 21:48 | +10 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-01 21:48 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 11-01 21:48 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-01 21:47 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-01 21:47 | +20 | BNB | DOWN | 0.56 | 0.86 | 2.73 |
| 11-01 21:47 | +15 | BNB | DOWN | 0.56 | 0.86 | 2.73 |
| 11-01 21:47 | +10 | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-01 21:47 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 11-01 21:47 | +10 stop | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 11-01 21:47 | +20 | SOL | DOWN | 0.58 | 0.82 | 2.11 |
| 11-01 21:47 | +15 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 11-01 21:47 | +10 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 11-01 21:47 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 11-01 21:47 | +10 stop | DOGE | DOWN | 0.57 | 0.73 | 1.31 |
| 11-01 21:47 | +20 | DOGE | DOWN | 0.55 | 0.76 | 1.76 |
| 11-01 21:47 | +15 | DOGE | DOWN | 0.55 | 0.73 | 1.45 |
| 11-01 21:47 | +10 | DOGE | DOWN | 0.55 | 0.73 | 1.45 |
| 11-01 21:47 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.30 |
| 11-01 21:46 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 11-01 21:46 | +20 | BTC | UP | 0.51 | open |  |
