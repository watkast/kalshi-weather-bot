# Range-Scalp Bot

*Updated Thu Oct 08 12:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7524 | 6517 | 1007 (13) | 3 | $-2361.76 | -5.0% |
| **+10¢** | 5707 | 4519 | 1188 (22) | 4 | $-2323.94 | -6.5% |
| **+15¢** | 4791 | 3538 | 1253 (30) | 3 | $-1940.90 | -6.5% |
| **+20¢** | 4279 | 2980 | 1299 (37) | 5 | $-1547.18 | -5.8% |
| **+10¢ (15¢ stop)** | 9118 | 9091 | 27 (17) | 4 | $-3313.04 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 12:01 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-08 12:01 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-08 12:01 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-08 12:01 | +10 stop | SOL | UP | 0.53 | open |  |
| 10-08 12:01 | +20 | SOL | UP | 0.55 | open |  |
| 10-08 12:01 | +15 | SOL | UP | 0.55 | open |  |
| 10-08 12:01 | +10 | SOL | UP | 0.55 | open |  |
| 10-08 12:01 | +5 | SOL | UP | 0.55 | open |  |
| 10-08 12:01 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-08 12:01 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-08 12:01 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.24 |
| 10-08 12:01 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-08 12:01 | +10 stop | HYPE | DOWN | 0.62 | open |  |
| 10-08 12:01 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-08 12:01 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-08 12:01 | +10 | HYPE | DOWN | 0.60 | open |  |
| 10-08 12:01 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-08 12:01 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 12:01 | +20 | BNB | DOWN | 0.52 | open |  |
| 10-08 12:01 | +15 | BNB | DOWN | 0.52 | 0.70 | 1.47 |
| 10-08 12:01 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 12:01 | +5 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 10-08 12:01 | +10 stop | BTC | DOWN | 0.45 | 0.56 | 0.74 |
| 10-08 12:01 | +20 | BTC | DOWN | 0.45 | open |  |
| 10-08 12:01 | +15 | BTC | DOWN | 0.45 | open |  |
| 10-08 12:01 | +10 | BTC | DOWN | 0.45 | 0.56 | 0.74 |
| 10-08 12:01 | +5 | BTC | DOWN | 0.45 | 0.56 | 0.74 |
| 10-08 12:01 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-08 12:01 | +20 | ETH | DOWN | 0.56 | open |  |
| 10-08 12:01 | +15 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 10-08 12:01 | +10 | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-08 12:01 | +5 | ETH | DOWN | 0.56 | 0.64 | 0.45 |
| 10-08 11:58 | +10 stop | ZEC | UP | 0.53 | 0.36 | -2.05 |
| 10-08 11:55 | +5 | DOGE | DOWN | 0.64 | 0.75 | 0.75 |
| 10-08 11:54 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-08 11:54 | +20 | DOGE | DOWN | 0.60 | 0.86 | 2.34 |
| 10-08 11:54 | +15 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-08 11:54 | +10 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-08 11:54 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-08 11:54 | +10 stop | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
