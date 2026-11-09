# Range-Scalp Bot

*Updated Mon Nov 09 03:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53234 | 46414 | 6820 (85) | 3 | $-14725.20 | -4.4% |
| **+10¢** | 39754 | 31799 | 7955 (110) | 2 | $-13729.33 | -5.5% |
| **+15¢** | 33310 | 24739 | 8571 (141) | 6 | $-12541.23 | -6.0% |
| **+20¢** | 29631 | 20644 | 8987 (186) | 7 | $-11052.75 | -6.0% |
| **+10¢ (15¢ stop)** | 64857 | 64751 | 106 (63) | 1 | $-24050.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 03:34 | +5 | ETH | UP | 0.65 | open |  |
| 11-09 03:33 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 11-09 03:33 | +10 stop | HYPE | DOWN | 0.52 | open |  |
| 11-09 03:33 | +15 | HYPE | DOWN | 0.52 | open |  |
| 11-09 03:33 | +10 | HYPE | DOWN | 0.52 | open |  |
| 11-09 03:33 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-09 03:33 | +20 | DOGE | UP | 0.69 | open |  |
| 11-09 03:33 | +15 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-09 03:33 | +10 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-09 03:33 | +5 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-09 03:32 | +10 stop | BNB | UP | 0.61 | 0.46 | -1.90 |
| 11-09 03:32 | +20 | BNB | UP | 0.61 | open |  |
| 11-09 03:32 | +15 | BNB | UP | 0.61 | open |  |
| 11-09 03:32 | +10 | BNB | UP | 0.61 | 0.74 | 0.94 |
| 11-09 03:32 | +5 | BNB | UP | 0.61 | 0.74 | 0.94 |
| 11-09 03:32 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 11-09 03:32 | +20 | SOL | UP | 0.63 | open |  |
| 11-09 03:32 | +15 | SOL | UP | 0.63 | open |  |
| 11-09 03:32 | +10 | SOL | UP | 0.63 | 0.75 | 0.89 |
| 11-09 03:32 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 11-09 03:32 | +5 | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 11-09 03:32 | +10 stop | ETH | UP | 0.51 | 0.63 | 0.85 |
| 11-09 03:32 | +10 | ETH | UP | 0.51 | 0.63 | 0.85 |
| 11-09 03:32 | +5 | ETH | UP | 0.51 | 0.59 | 0.45 |
| 11-09 03:32 | +10 stop | BTC | UP | 0.54 | 0.30 | -2.73 |
| 11-09 03:32 | +20 | BTC | UP | 0.54 | open |  |
| 11-09 03:32 | +15 | BTC | UP | 0.54 | open |  |
| 11-09 03:32 | +10 | BTC | UP | 0.54 | open |  |
| 11-09 03:32 | +5 | BTC | UP | 0.54 | open |  |
| 11-09 03:32 | +5 | HYPE | UP | 0.64 | open |  |
| 11-09 03:31 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-09 03:31 | +20 | ETH | UP | 0.58 | open |  |
| 11-09 03:31 | +15 | ETH | UP | 0.58 | open |  |
| 11-09 03:31 | +10 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-09 03:31 | +5 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-09 03:31 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-09 03:31 | +20 | NEAR | UP | 0.69 | open |  |
| 11-09 03:31 | +15 | NEAR | UP | 0.69 | open |  |
| 11-09 03:31 | +10 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-09 03:31 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
