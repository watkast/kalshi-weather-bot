# Range-Scalp Bot

*Updated Tue Nov 10 22:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55005 | 47968 | 7037 (94) | 5 | $-15048.29 | -4.3% |
| **+10¢** | 41103 | 32897 | 8206 (124) | 5 | $-13946.54 | -5.4% |
| **+15¢** | 34458 | 25617 | 8841 (158) | 7 | $-12659.04 | -5.9% |
| **+20¢** | 30673 | 21397 | 9276 (207) | 7 | $-11083.70 | -5.8% |
| **+10¢ (15¢ stop)** | 67023 | 66905 | 118 (73) | 0 | $-24779.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 22:53 | +10 stop | HYPE | DOWN | 0.51 | 0.71 | 1.71 |
| 11-10 22:52 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-10 22:51 | +5 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 22:51 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-10 22:50 | +5 | SOL | UP | 0.67 | 0.75 | 0.50 |
| 11-10 22:50 | +10 stop | HYPE | DOWN | 0.62 | 0.37 | -2.84 |
| 11-10 22:50 | +10 stop | SOL | UP | 0.62 | 0.75 | 0.99 |
| 11-10 22:50 | +15 | SOL | UP | 0.62 | open |  |
| 11-10 22:50 | +10 | SOL | UP | 0.62 | 0.75 | 0.99 |
| 11-10 22:50 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-10 22:48 | +10 stop | NEAR | UP | 0.63 | 0.43 | -2.35 |
| 11-10 22:48 | +10 stop | DOGE | UP | 0.65 | 0.82 | 1.43 |
| 11-10 22:48 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-10 22:48 | +10 stop | BNB | UP | 0.62 | 0.76 | 1.10 |
| 11-10 22:48 | +10 stop | HYPE | UP | 0.69 | 0.45 | -2.73 |
| 11-10 22:48 | +20 | HYPE | UP | 0.69 | open |  |
| 11-10 22:48 | +15 | HYPE | UP | 0.69 | open |  |
| 11-10 22:48 | +10 | HYPE | UP | 0.69 | open |  |
| 11-10 22:48 | +5 | HYPE | UP | 0.69 | open |  |
| 11-10 22:47 | +10 stop | XRP | UP | 0.54 | 0.64 | 0.65 |
| 11-10 22:47 | +20 | XRP | UP | 0.54 | 0.77 | 1.99 |
| 11-10 22:47 | +15 | XRP | UP | 0.54 | 0.73 | 1.58 |
| 11-10 22:47 | +10 | XRP | UP | 0.54 | 0.64 | 0.65 |
| 11-10 22:47 | +5 | XRP | UP | 0.54 | 0.64 | 0.65 |
| 11-10 22:47 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-10 22:47 | +20 | SOL | UP | 0.61 | open |  |
| 11-10 22:47 | +15 | SOL | UP | 0.61 | 0.79 | 1.51 |
| 11-10 22:47 | +10 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-10 22:47 | +5 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-10 22:46 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.98 |
| 11-10 22:46 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-10 22:46 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-10 22:46 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-10 22:46 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-10 22:46 | +10 stop | BTC | DOWN | 0.57 | 0.36 | -2.45 |
| 11-10 22:46 | +20 | BTC | DOWN | 0.57 | open |  |
| 11-10 22:46 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-10 22:46 | +10 | BTC | DOWN | 0.57 | open |  |
| 11-10 22:46 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-10 22:46 | +10 stop | BNB | DOWN | 0.59 | 0.40 | -2.23 |
