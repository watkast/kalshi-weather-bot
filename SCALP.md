# Range-Scalp Bot

*Updated Tue Nov 10 23:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55058 | 48017 | 7041 (94) | 5 | $-15044.71 | -4.3% |
| **+10¢** | 41143 | 32933 | 8210 (124) | 5 | $-13932.49 | -5.4% |
| **+15¢** | 34492 | 25644 | 8848 (158) | 5 | $-12662.15 | -5.9% |
| **+20¢** | 30704 | 21421 | 9283 (207) | 5 | $-11078.59 | -5.8% |
| **+10¢ (15¢ stop)** | 67068 | 66950 | 118 (73) | 5 | $-24767.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 23:45 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +20 | DOGE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-10 23:45 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-10 23:45 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-10 23:45 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-10 23:45 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-10 23:45 | +10 stop | NEAR | DOWN | 0.53 | open |  |
| 11-10 23:45 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-10 23:45 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-10 23:45 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-10 23:45 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-10 23:45 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 11-10 23:45 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-10 23:45 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-10 23:45 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-10 23:45 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-10 23:45 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-10 23:45 | +10 | HYPE | DOWN | 0.61 | open |  |
| 11-10 23:45 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-10 23:37 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-10 23:36 | +5 | ETH | UP | 0.63 | 0.70 | 0.38 |
| 11-10 23:36 | +10 stop | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 11-10 23:35 | +10 stop | ZEC | UP | 0.64 | 0.78 | 1.08 |
| 11-10 23:35 | +10 | ZEC | UP | 0.64 | 0.78 | 1.08 |
| 11-10 23:35 | +5 | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 11-10 23:34 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 11-10 23:34 | +10 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 11-10 23:34 | +5 | XRP | UP | 0.57 | 0.62 | 0.15 |
| 11-10 23:34 | +5 | NEAR | DOWN | 0.56 | yes | -5.78 |
| 11-10 23:34 | +10 stop | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-10 23:34 | +15 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-10 23:34 | +10 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-10 23:34 | +5 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-10 23:33 | +5 | BTC | UP | 0.60 | 0.69 | 0.58 |
