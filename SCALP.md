# Range-Scalp Bot

*Updated Thu Nov 05 17:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48660 | 42412 | 6248 (73) | 5 | $-13764.28 | -4.5% |
| **+10¢** | 36318 | 29056 | 7262 (99) | 7 | $-12619.77 | -5.5% |
| **+15¢** | 30412 | 22590 | 7822 (127) | 8 | $-11525.34 | -6.0% |
| **+20¢** | 27017 | 18821 | 8196 (166) | 8 | $-10178.93 | -6.0% |
| **+10¢ (15¢ stop)** | 59298 | 59205 | 93 (56) | 2 | $-21961.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 17:41 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-05 17:41 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-05 17:41 | +10 stop | NEAR | UP | 0.57 | open |  |
| 11-05 17:41 | +20 | NEAR | UP | 0.57 | open |  |
| 11-05 17:41 | +15 | NEAR | UP | 0.57 | open |  |
| 11-05 17:41 | +10 | NEAR | UP | 0.57 | open |  |
| 11-05 17:41 | +5 | NEAR | UP | 0.57 | open |  |
| 11-05 17:41 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 11-05 17:41 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-05 17:41 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 11-05 17:40 | +10 stop | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-05 17:40 | +5 | BTC | DOWN | 0.53 | 0.61 | 0.45 |
| 11-05 17:40 | +10 stop | BTC | UP | 0.51 | 0.36 | -1.85 |
| 11-05 17:40 | +15 | BTC | UP | 0.51 | open |  |
| 11-05 17:40 | +10 | BTC | UP | 0.51 | open |  |
| 11-05 17:40 | +5 | BTC | UP | 0.52 | 0.60 | 0.45 |
| 11-05 17:40 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-05 17:39 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.91 |
| 11-05 17:39 | +10 stop | ETH | UP | 0.66 | 0.45 | -2.44 |
| 11-05 17:39 | +10 | ETH | UP | 0.66 | open |  |
| 11-05 17:39 | +5 | ETH | UP | 0.66 | open |  |
| 11-05 17:39 | +10 stop | SOL | UP | 0.61 | 0.45 | -1.95 |
| 11-05 17:37 | +10 stop | ETH | UP | 0.58 | 0.76 | 1.49 |
| 11-05 17:37 | +10 | ETH | UP | 0.58 | 0.76 | 1.49 |
| 11-05 17:37 | +5 | ETH | UP | 0.58 | 0.76 | 1.49 |
| 11-05 17:37 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 17:37 | +15 | DOGE | UP | 0.65 | open |  |
| 11-05 17:37 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 17:37 | +5 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 11-05 17:37 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-05 17:37 | +10 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-05 17:37 | +5 | ETH | UP | 0.60 | 0.69 | 0.58 |
| 11-05 17:37 | +10 stop | HYPE | UP | 0.65 | 0.49 | -1.94 |
| 11-05 17:37 | +10 | HYPE | UP | 0.65 | open |  |
| 11-05 17:37 | +5 | HYPE | UP | 0.65 | open |  |
| 11-05 17:37 | +10 stop | BNB | UP | 0.65 | 0.49 | -1.90 |
| 11-05 17:37 | +10 | BNB | UP | 0.65 | open |  |
| 11-05 17:37 | +5 | BNB | UP | 0.65 | open |  |
| 11-05 17:36 | +10 stop | SOL | UP | 0.67 | 0.52 | -1.84 |
| 11-05 17:36 | +15 | SOL | UP | 0.67 | open |  |
