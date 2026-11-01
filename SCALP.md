# Range-Scalp Bot

*Updated Sun Nov 01 17:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43723 | 38103 | 5620 (64) | 6 | $-12446.76 | -4.5% |
| **+10¢** | 32617 | 26125 | 6492 (85) | 7 | $-11170.42 | -5.4% |
| **+15¢** | 27298 | 20305 | 6993 (112) | 7 | $-10211.69 | -6.0% |
| **+20¢** | 24241 | 16915 | 7326 (146) | 7 | $-9015.43 | -5.9% |
| **+10¢ (15¢ stop)** | 53331 | 53245 | 86 (51) | 1 | $-20127.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 17:18 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 11-01 17:18 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 17:17 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 17:17 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 17:17 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 17:17 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-01 17:16 | +10 stop | ETH | UP | 0.52 | 0.62 | 0.65 |
| 11-01 17:16 | +20 | ETH | UP | 0.52 | open |  |
| 11-01 17:16 | +15 | ETH | UP | 0.52 | open |  |
| 11-01 17:16 | +10 | ETH | UP | 0.53 | open |  |
| 11-01 17:16 | +5 | ETH | UP | 0.53 | 0.62 | 0.55 |
| 11-01 17:16 | +10 stop | DOGE | UP | 0.58 | 0.32 | -2.91 |
| 11-01 17:16 | +20 | DOGE | UP | 0.57 | open |  |
| 11-01 17:16 | +15 | DOGE | UP | 0.57 | open |  |
| 11-01 17:16 | +10 | DOGE | UP | 0.58 | open |  |
| 11-01 17:16 | +5 | DOGE | UP | 0.58 | open |  |
| 11-01 17:16 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.95 |
| 11-01 17:16 | +20 | HYPE | UP | 0.54 | open |  |
| 11-01 17:16 | +15 | HYPE | UP | 0.54 | open |  |
| 11-01 17:16 | +10 | HYPE | UP | 0.54 | open |  |
| 11-01 17:16 | +5 | HYPE | UP | 0.54 | open |  |
| 11-01 17:16 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 17:16 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.81 |
| 11-01 17:16 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-01 17:16 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 17:16 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 17:16 | +10 stop | ZEC | UP | 0.58 | 0.43 | -1.86 |
| 11-01 17:16 | +20 | ZEC | UP | 0.58 | open |  |
| 11-01 17:16 | +15 | ZEC | UP | 0.58 | open |  |
| 11-01 17:16 | +10 | ZEC | UP | 0.58 | open |  |
| 11-01 17:16 | +5 | ZEC | UP | 0.58 | open |  |
| 11-01 17:16 | +10 stop | BTC | UP | 0.63 | 0.35 | -3.13 |
| 11-01 17:16 | +20 | BTC | UP | 0.63 | open |  |
| 11-01 17:16 | +15 | BTC | UP | 0.63 | open |  |
| 11-01 17:16 | +10 | BTC | UP | 0.63 | open |  |
| 11-01 17:16 | +5 | BTC | UP | 0.63 | open |  |
| 11-01 17:16 | +10 stop | XRP | UP | 0.62 | 0.39 | -2.69 |
| 11-01 17:16 | +20 | XRP | UP | 0.62 | open |  |
| 11-01 17:16 | +15 | XRP | UP | 0.62 | open |  |
| 11-01 17:16 | +10 | XRP | UP | 0.62 | open |  |
