# Range-Scalp Bot

*Updated Sat Oct 10 22:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11009 | 9494 | 1515 (22) | 5 | $-3732.86 | -5.4% |
| **+10¢** | 8331 | 6567 | 1764 (36) | 7 | $-3559.21 | -6.8% |
| **+15¢** | 7024 | 5158 | 1866 (52) | 8 | $-2997.77 | -6.8% |
| **+20¢** | 6250 | 4307 | 1943 (66) | 8 | $-2533.08 | -6.5% |
| **+10¢ (15¢ stop)** | 13568 | 13527 | 41 (25) | 1 | $-5458.24 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 22:38 | +10 stop | XRP | UP | 0.65 | 0.39 | -2.93 |
| 10-10 22:37 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-10 22:37 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-10 22:36 | +10 stop | BNB | UP | 0.52 | 0.78 | 2.29 |
| 10-10 22:36 | +5 | BNB | UP | 0.58 | 0.78 | 1.69 |
| 10-10 22:36 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 10-10 22:36 | +10 stop | XRP | DOWN | 0.62 | 0.44 | -2.15 |
| 10-10 22:35 | +10 stop | ZEC | UP | 0.64 | 0.77 | 1.00 |
| 10-10 22:34 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 10-10 22:34 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.91 |
| 10-10 22:34 | +10 stop | DOGE | UP | 0.65 | 0.47 | -2.16 |
| 10-10 22:33 | +10 stop | NEAR | UP | 0.58 | 0.72 | 1.11 |
| 10-10 22:33 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 10-10 22:33 | +15 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-10 22:33 | +10 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-10 22:33 | +5 | NEAR | UP | 0.57 | 0.66 | 0.57 |
| 10-10 22:33 | +10 stop | HYPE | UP | 0.58 | 0.72 | 1.03 |
| 10-10 22:33 | +5 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 10-10 22:32 | +10 stop | ZEC | DOWN | 0.52 | 0.34 | -2.14 |
| 10-10 22:32 | +20 | ZEC | DOWN | 0.52 | open |  |
| 10-10 22:32 | +15 | ZEC | DOWN | 0.52 | open |  |
| 10-10 22:32 | +10 | ZEC | DOWN | 0.52 | open |  |
| 10-10 22:32 | +5 | ZEC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-10 22:31 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.73 |
| 10-10 22:31 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-10 22:31 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-10 22:31 | +10 | SOL | DOWN | 0.65 | open |  |
| 10-10 22:31 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-10 22:31 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-10 22:31 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-10 22:31 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-10 22:31 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-10 22:31 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-10 22:31 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-10 22:31 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-10 22:31 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-10 22:31 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-10 22:31 | +5 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 10-10 22:31 | +10 stop | DOGE | DOWN | 0.61 | 0.42 | -2.22 |
| 10-10 22:31 | +20 | DOGE | DOWN | 0.61 | open |  |
