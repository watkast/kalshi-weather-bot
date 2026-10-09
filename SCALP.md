# Range-Scalp Bot

*Updated Fri Oct 09 11:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8981 | 7763 | 1218 (14) | 1 | $-2978.73 | -5.3% |
| **+10¢** | 6792 | 5367 | 1425 (26) | 4 | $-2843.27 | -6.6% |
| **+15¢** | 5729 | 4228 | 1501 (38) | 5 | $-2312.90 | -6.4% |
| **+20¢** | 5100 | 3543 | 1557 (46) | 5 | $-1903.13 | -5.9% |
| **+10¢ (15¢ stop)** | 10930 | 10900 | 30 (19) | 4 | $-4102.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 11:02 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-09 11:02 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-09 11:02 | +10 stop | NEAR | DOWN | 0.61 | open |  |
| 10-09 11:02 | +5 | NEAR | DOWN | 0.60 | open |  |
| 10-09 11:02 | +10 stop | XRP | DOWN | 0.60 | open |  |
| 10-09 11:02 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-09 11:02 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-09 11:02 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-09 11:02 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 10-09 11:02 | +10 stop | ZEC | DOWN | 0.67 | open |  |
| 10-09 11:02 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-09 11:02 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-09 11:02 | +10 | ZEC | DOWN | 0.67 | open |  |
| 10-09 11:02 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.24 |
| 10-09 11:02 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
| 10-09 11:02 | +10 stop | HYPE | UP | 0.43 | 0.54 | 0.74 |
| 10-09 11:02 | +10 | HYPE | UP | 0.43 | 0.54 | 0.74 |
| 10-09 11:02 | +5 | HYPE | UP | 0.43 | 0.54 | 0.74 |
| 10-09 11:01 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-09 11:01 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-09 11:01 | +15 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-09 11:01 | +10 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-09 11:01 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 10-09 11:01 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-09 11:01 | +20 | ETH | DOWN | 0.57 | open |  |
| 10-09 11:01 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-09 11:01 | +10 | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 10-09 11:01 | +5 | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 10-09 11:00 | +10 stop | NEAR | DOWN | 0.63 | 0.45 | -2.15 |
| 10-09 11:00 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-09 11:00 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-09 11:00 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-09 11:00 | +5 | NEAR | DOWN | 0.63 | 0.72 | 0.58 |
| 10-09 11:00 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 11:00 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-09 11:00 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-09 11:00 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 11:00 | +5 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 10-09 10:58 | +10 stop | DOGE | UP | 0.44 | 0.63 | 1.55 |
| 10-09 10:57 | +10 stop | ETH | DOWN | 0.49 | 0.64 | 1.15 |
