# Range-Scalp Bot

*Updated Wed Nov 04 01:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46611 | 40589 | 6022 (72) | 6 | $-13396.51 | -4.6% |
| **+10¢** | 34813 | 27834 | 6979 (96) | 6 | $-12213.86 | -5.6% |
| **+15¢** | 29151 | 21642 | 7509 (124) | 6 | $-11172.84 | -6.1% |
| **+20¢** | 25896 | 18030 | 7866 (164) | 7 | $-9844.63 | -6.1% |
| **+10¢ (15¢ stop)** | 56829 | 56736 | 93 (56) | 4 | $-21249.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 01:35 | +10 stop | SOL | UP | 0.61 | open |  |
| 11-04 01:35 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-04 01:35 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-04 01:35 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-04 01:35 | +5 | DOGE | DOWN | 0.67 | open |  |
| 11-04 01:34 | +5 | XRP | DOWN | 0.55 | open |  |
| 11-04 01:34 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 11-04 01:34 | +10 | BTC | DOWN | 0.53 | open |  |
| 11-04 01:34 | +5 | BTC | DOWN | 0.54 | open |  |
| 11-04 01:34 | +10 stop | NEAR | DOWN | 0.71 | 0.55 | -1.93 |
| 11-04 01:34 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-04 01:34 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-04 01:34 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-04 01:34 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-04 01:34 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 11-04 01:34 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-04 01:34 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-04 01:34 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-04 01:34 | +5 | ETH | DOWN | 0.65 | open |  |
| 11-04 01:33 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.53 |
| 11-04 01:33 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-04 01:33 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-04 01:32 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 11-04 01:32 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-04 01:32 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-04 01:32 | +10 | XRP | DOWN | 0.62 | open |  |
| 11-04 01:32 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-04 01:32 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 01:32 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-04 01:32 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 01:32 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-04 01:31 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 01:31 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 01:31 | +10 stop | SOL | DOWN | 0.54 | 0.67 | 0.96 |
| 11-04 01:31 | +20 | SOL | DOWN | 0.54 | open |  |
| 11-04 01:31 | +15 | SOL | DOWN | 0.54 | open |  |
| 11-04 01:31 | +10 | SOL | DOWN | 0.54 | 0.67 | 0.96 |
| 11-04 01:31 | +5 | SOL | DOWN | 0.54 | 0.61 | 0.35 |
| 11-04 01:31 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 01:31 | +20 | BTC | DOWN | 0.62 | open |  |
