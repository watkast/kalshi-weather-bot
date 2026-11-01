# Range-Scalp Bot

*Updated Sun Nov 01 05:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43268 | 37717 | 5551 (62) | 3 | $-12288.55 | -4.5% |
| **+10¢** | 32268 | 25855 | 6413 (84) | 3 | $-10992.64 | -5.4% |
| **+15¢** | 27001 | 20090 | 6911 (112) | 3 | $-10051.22 | -5.9% |
| **+20¢** | 23979 | 16738 | 7241 (146) | 5 | $-8874.06 | -5.9% |
| **+10¢ (15¢ stop)** | 52745 | 52662 | 83 (48) | 3 | $-19908.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 05:33 | +5 | NEAR | UP | 0.63 | open |  |
| 11-01 05:32 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 11-01 05:32 | +10 | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 11-01 05:32 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 11-01 05:31 | +5 | BNB | UP | 0.66 | open |  |
| 11-01 05:31 | +5 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-01 05:31 | +10 stop | HYPE | DOWN | 0.54 | open |  |
| 11-01 05:31 | +20 | HYPE | DOWN | 0.54 | open |  |
| 11-01 05:31 | +15 | HYPE | DOWN | 0.54 | open |  |
| 11-01 05:31 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-01 05:31 | +5 | HYPE | DOWN | 0.54 | open |  |
| 11-01 05:31 | +10 stop | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-01 05:31 | +20 | ETH | UP | 0.64 | open |  |
| 11-01 05:31 | +15 | ETH | UP | 0.64 | 0.81 | 1.42 |
| 11-01 05:31 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-01 05:31 | +5 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-01 05:31 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-01 05:31 | +20 | BNB | UP | 0.60 | open |  |
| 11-01 05:31 | +15 | BNB | UP | 0.60 | open |  |
| 11-01 05:31 | +10 | BNB | UP | 0.60 | open |  |
| 11-01 05:31 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 11-01 05:31 | +10 stop | XRP | UP | 0.57 | 0.72 | 1.17 |
| 11-01 05:31 | +20 | XRP | UP | 0.57 | 0.78 | 1.79 |
| 11-01 05:31 | +15 | XRP | UP | 0.57 | 0.72 | 1.17 |
| 11-01 05:31 | +10 | XRP | UP | 0.57 | 0.72 | 1.17 |
| 11-01 05:31 | +5 | XRP | UP | 0.57 | 0.72 | 1.17 |
| 11-01 05:31 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-01 05:31 | +20 | NEAR | UP | 0.58 | open |  |
| 11-01 05:31 | +15 | NEAR | UP | 0.58 | open |  |
| 11-01 05:31 | +10 | NEAR | UP | 0.58 | open |  |
| 11-01 05:31 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 11-01 05:31 | +10 stop | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 11-01 05:31 | +20 | DOGE | UP | 0.60 | 0.80 | 1.71 |
| 11-01 05:31 | +15 | DOGE | UP | 0.60 | 0.75 | 1.19 |
| 11-01 05:31 | +10 | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 11-01 05:31 | +5 | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 11-01 05:31 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-01 05:31 | +20 | BTC | UP | 0.70 | open |  |
| 11-01 05:31 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-01 05:31 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
