# Range-Scalp Bot

*Updated Wed Oct 28 13:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38171 | 33303 | 4868 (46) | 3 | $-10775.86 | -4.5% |
| **+10¢** | 28473 | 22844 | 5629 (68) | 3 | $-9614.78 | -5.4% |
| **+15¢** | 23819 | 17776 | 6043 (93) | 5 | $-8562.44 | -5.7% |
| **+20¢** | 21128 | 14799 | 6329 (118) | 5 | $-7532.04 | -5.7% |
| **+10¢ (15¢ stop)** | 46728 | 46661 | 67 (35) | 3 | $-17764.56 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 13:33 | +5 | DOGE | UP | 0.67 | open |  |
| 10-28 13:33 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 10-28 13:33 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-28 13:33 | +15 | SOL | UP | 0.65 | open |  |
| 10-28 13:33 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-28 13:33 | +5 | SOL | UP | 0.65 | 0.73 | 0.50 |
| 10-28 13:33 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-28 13:33 | +20 | ETH | UP | 0.64 | open |  |
| 10-28 13:33 | +15 | ETH | UP | 0.64 | open |  |
| 10-28 13:33 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-28 13:33 | +5 | ETH | UP | 0.65 | 0.72 | 0.39 |
| 10-28 13:33 | +10 stop | DOGE | UP | 0.58 | open |  |
| 10-28 13:33 | +20 | DOGE | UP | 0.58 | open |  |
| 10-28 13:33 | +15 | DOGE | UP | 0.58 | open |  |
| 10-28 13:33 | +10 | DOGE | UP | 0.58 | open |  |
| 10-28 13:33 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
| 10-28 13:32 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-28 13:32 | +10 | BTC | UP | 0.67 | open |  |
| 10-28 13:31 | +5 | BTC | UP | 0.67 | open |  |
| 10-28 13:31 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.91 |
| 10-28 13:31 | +20 | BNB | UP | 0.57 | open |  |
| 10-28 13:31 | +15 | BNB | UP | 0.57 | open |  |
| 10-28 13:31 | +10 | BNB | UP | 0.57 | open |  |
| 10-28 13:31 | +5 | BNB | UP | 0.57 | open |  |
| 10-28 13:31 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-28 13:31 | +20 | SOL | UP | 0.62 | open |  |
| 10-28 13:31 | +15 | SOL | UP | 0.62 | 0.79 | 1.41 |
| 10-28 13:31 | +10 | SOL | UP | 0.64 | 0.76 | 0.90 |
| 10-28 13:31 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 10-28 13:31 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-28 13:31 | +20 | BTC | UP | 0.57 | open |  |
| 10-28 13:31 | +15 | BTC | UP | 0.55 | open |  |
| 10-28 13:31 | +10 | BTC | UP | 0.53 | 0.67 | 1.06 |
| 10-28 13:31 | +5 | BTC | UP | 0.52 | 0.60 | 0.45 |
| 10-28 13:26 | +5 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-28 13:26 | +10 stop | XRP | DOWN | 0.60 | 0.85 | 2.24 |
| 10-28 13:25 | +5 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-28 13:25 | +10 stop | ZEC | DOWN | 0.65 | 0.49 | -1.94 |
| 10-28 13:24 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-28 13:22 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
