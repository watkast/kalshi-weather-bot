# Range-Scalp Bot

*Updated Tue Nov 10 23:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55070 | 48029 | 7041 (94) | 4 | $-15038.59 | -4.3% |
| **+10¢** | 41153 | 32943 | 8210 (124) | 4 | $-13922.47 | -5.4% |
| **+15¢** | 34500 | 25652 | 8848 (158) | 4 | $-12650.56 | -5.8% |
| **+20¢** | 30712 | 21429 | 9283 (207) | 4 | $-11063.67 | -5.7% |
| **+10¢ (15¢ stop)** | 67084 | 66966 | 118 (73) | 3 | $-24761.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 23:55 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 11-10 23:55 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-10 23:55 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-10 23:55 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-10 23:55 | +5 | XRP | DOWN | 0.67 | open |  |
| 11-10 23:54 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-10 23:54 | +10 stop | SOL | DOWN | 0.55 | open |  |
| 11-10 23:53 | +10 stop | DOGE | UP | 0.55 | open |  |
| 11-10 23:53 | +20 | DOGE | UP | 0.55 | open |  |
| 11-10 23:53 | +15 | DOGE | UP | 0.55 | open |  |
| 11-10 23:53 | +10 | DOGE | UP | 0.55 | open |  |
| 11-10 23:53 | +5 | DOGE | UP | 0.55 | open |  |
| 11-10 23:52 | +10 stop | HYPE | DOWN | 0.52 | 0.35 | -2.04 |
| 11-10 23:52 | +20 | HYPE | DOWN | 0.54 | open |  |
| 11-10 23:52 | +15 | HYPE | DOWN | 0.54 | open |  |
| 11-10 23:52 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-10 23:52 | +5 | HYPE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-10 23:49 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-10 23:49 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 23:49 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-10 23:49 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 23:49 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 23:49 | +10 stop | DOGE | DOWN | 0.53 | 0.69 | 1.27 |
| 11-10 23:48 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-10 23:48 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-10 23:48 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-10 23:48 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-10 23:48 | +10 stop | BTC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-10 23:48 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-10 23:48 | +15 | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 11-10 23:48 | +10 | BTC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-10 23:48 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-10 23:48 | +10 stop | DOGE | DOWN | 0.48 | 0.59 | 0.75 |
| 11-10 23:47 | +10 stop | SOL | UP | 0.67 | 0.43 | -2.74 |
| 11-10 23:47 | +20 | SOL | UP | 0.67 | open |  |
| 11-10 23:47 | +15 | SOL | UP | 0.67 | open |  |
| 11-10 23:47 | +10 | SOL | UP | 0.67 | open |  |
| 11-10 23:47 | +5 | SOL | UP | 0.67 | open |  |
| 11-10 23:47 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-10 23:47 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
