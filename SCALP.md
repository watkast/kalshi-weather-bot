# Range-Scalp Bot

*Updated Tue Nov 17 14:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62887 | 54855 | 8032 (117) | 7 | $-17121.30 | -4.3% |
| **+10¢** | 46966 | 37568 | 9398 (159) | 8 | $-15995.76 | -5.4% |
| **+15¢** | 39365 | 29229 | 10136 (201) | 9 | $-14539.63 | -5.9% |
| **+20¢** | 35080 | 24451 | 10629 (256) | 9 | $-12714.75 | -5.8% |
| **+10¢ (15¢ stop)** | 76539 | 76383 | 156 (92) | 3 | $-28232.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 14:35 | +10 stop | NEAR | DOWN | 0.50 | 0.67 | 1.36 |
| 11-17 14:35 | +10 stop | DOGE | DOWN | 0.57 | open |  |
| 11-17 14:35 | +5 | DOGE | DOWN | 0.57 | 0.66 | 0.56 |
| 11-17 14:34 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-17 14:34 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +20 | ZEC | DOWN | 0.58 | open |  |
| 11-17 14:34 | +15 | ZEC | DOWN | 0.58 | open |  |
| 11-17 14:34 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 14:34 | +10 stop | ETH | DOWN | 0.67 | 0.51 | -1.93 |
| 11-17 14:34 | +10 stop | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-17 14:34 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-17 14:34 | +10 stop | HYPE | UP | 0.65 | 0.42 | -2.64 |
| 11-17 14:34 | +10 stop | SOL | UP | 0.60 | open |  |
| 11-17 14:33 | +10 stop | BNB | UP | 0.61 | 0.41 | -2.36 |
| 11-17 14:33 | +20 | BNB | UP | 0.62 | open |  |
| 11-17 14:33 | +15 | BNB | UP | 0.62 | open |  |
| 11-17 14:33 | +10 | BNB | UP | 0.61 | open |  |
| 11-17 14:33 | +10 stop | BTC | UP | 0.66 | 0.50 | -1.94 |
| 11-17 14:33 | +5 | BNB | UP | 0.61 | open |  |
| 11-17 14:33 | +10 stop | NEAR | UP | 0.64 | 0.44 | -2.33 |
| 11-17 14:33 | +5 | BNB | DOWN | 0.50 | 0.58 | 0.44 |
| 11-17 14:33 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 11-17 14:33 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-17 14:33 | +15 | ETH | DOWN | 0.69 | open |  |
| 11-17 14:33 | +10 | ETH | DOWN | 0.69 | open |  |
| 11-17 14:33 | +5 | ETH | DOWN | 0.69 | open |  |
| 11-17 14:33 | +10 stop | DOGE | DOWN | 0.58 | 0.39 | -2.25 |
| 11-17 14:33 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-17 14:33 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-17 14:33 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-17 14:33 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 11-17 14:32 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 11-17 14:32 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-17 14:32 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-17 14:32 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-17 14:32 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-17 14:32 | +10 stop | SOL | DOWN | 0.66 | 0.44 | -2.54 |
| 11-17 14:32 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-17 14:32 | +15 | SOL | DOWN | 0.64 | open |  |
