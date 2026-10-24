# Range-Scalp Bot

*Updated Sat Oct 24 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32204 | 28079 | 4125 (40) | 3 | $-9198.18 | -4.5% |
| **+10¢** | 24106 | 19330 | 4776 (58) | 4 | $-8227.38 | -5.4% |
| **+15¢** | 20185 | 15048 | 5137 (81) | 4 | $-7367.98 | -5.8% |
| **+20¢** | 17880 | 12503 | 5377 (103) | 5 | $-6536.62 | -5.8% |
| **+10¢ (15¢ stop)** | 39578 | 39519 | 59 (32) | 3 | $-15139.78 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 23:11 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-24 23:11 | +20 | BTC | UP | 0.58 | open |  |
| 10-24 23:11 | +15 | BTC | UP | 0.58 | open |  |
| 10-24 23:11 | +10 | BTC | UP | 0.59 | open |  |
| 10-24 23:11 | +5 | BTC | UP | 0.59 | open |  |
| 10-24 23:11 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-24 23:10 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-24 23:10 | +10 stop | SOL | UP | 0.53 | open |  |
| 10-24 23:10 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-24 23:10 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-24 23:09 | +10 stop | BNB | DOWN | 0.34 | 0.55 | 1.76 |
| 10-24 23:09 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-24 23:09 | +15 | XRP | DOWN | 0.48 | 0.91 | 4.00 |
| 10-24 23:09 | +10 | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-24 23:09 | +5 | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-24 23:09 | +10 stop | ETH | DOWN | 0.39 | 0.58 | 1.55 |
| 10-24 23:09 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-24 23:09 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-24 23:09 | +15 | NEAR | DOWN | 0.65 | 0.83 | 1.54 |
| 10-24 23:09 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 23:09 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 10-24 23:08 | +10 stop | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 10-24 23:08 | +20 | XRP | DOWN | 0.48 | 0.91 | 4.00 |
| 10-24 23:08 | +15 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 10-24 23:08 | +10 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 10-24 23:08 | +5 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 10-24 23:08 | +10 stop | SOL | DOWN | 0.67 | 0.43 | -2.74 |
| 10-24 23:08 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-24 23:08 | +15 | SOL | DOWN | 0.68 | open |  |
| 10-24 23:08 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-24 23:08 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-24 23:08 | +10 stop | BNB | DOWN | 0.58 | 0.36 | -2.55 |
| 10-24 23:08 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-24 23:08 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-24 23:08 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-24 23:08 | +5 | BNB | DOWN | 0.58 | open |  |
| 10-24 23:08 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 10-24 23:08 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-24 23:08 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-24 23:08 | +10 | ETH | DOWN | 0.68 | open |  |
