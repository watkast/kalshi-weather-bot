# Range-Scalp Bot

*Updated Sat Nov 14 08:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59232 | 51682 | 7550 (107) | 2 | $-15996.28 | -4.3% |
| **+10¢** | 44251 | 35416 | 8835 (140) | 2 | $-15014.21 | -5.4% |
| **+15¢** | 37081 | 27554 | 9527 (176) | 2 | $-13650.45 | -5.9% |
| **+20¢** | 33031 | 23029 | 10002 (228) | 2 | $-12047.81 | -5.8% |
| **+10¢ (15¢ stop)** | 72084 | 71942 | 142 (82) | 0 | $-26500.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 08:54 | +10 stop | NEAR | DOWN | 0.53 | 0.71 | 1.47 |
| 11-14 08:53 | +10 stop | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 11-14 08:52 | +5 | NEAR | UP | 0.71 | open |  |
| 11-14 08:51 | +10 stop | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 08:49 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-14 08:49 | +20 | SOL | DOWN | 0.63 | 0.85 | 1.94 |
| 11-14 08:49 | +15 | SOL | DOWN | 0.63 | 0.85 | 1.94 |
| 11-14 08:49 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-14 08:49 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 11-14 08:49 | +10 stop | NEAR | UP | 0.66 | 0.41 | -2.83 |
| 11-14 08:49 | +15 | NEAR | UP | 0.66 | open |  |
| 11-14 08:49 | +10 | NEAR | UP | 0.66 | open |  |
| 11-14 08:49 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 11-14 08:48 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-14 08:47 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
| 11-14 08:47 | +20 | XRP | UP | 0.67 | open |  |
| 11-14 08:47 | +15 | XRP | UP | 0.67 | open |  |
| 11-14 08:47 | +10 | XRP | UP | 0.67 | open |  |
| 11-14 08:47 | +5 | XRP | UP | 0.67 | open |  |
| 11-14 08:47 | +10 stop | DOGE | DOWN | 0.50 | 0.70 | 1.67 |
| 11-14 08:47 | +20 | DOGE | DOWN | 0.50 | 0.70 | 1.67 |
| 11-14 08:47 | +15 | DOGE | DOWN | 0.50 | 0.70 | 1.67 |
| 11-14 08:47 | +10 | DOGE | DOWN | 0.50 | 0.70 | 1.67 |
| 11-14 08:47 | +5 | DOGE | DOWN | 0.50 | 0.70 | 1.67 |
| 11-14 08:46 | +10 stop | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-14 08:46 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-14 08:46 | +15 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-14 08:46 | +10 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-14 08:46 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-14 08:46 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 08:46 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 11-14 08:46 | +15 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 11-14 08:46 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 08:46 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 08:46 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 08:46 | +20 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 08:46 | +15 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 11-14 08:46 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 08:46 | +5 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 08:46 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
