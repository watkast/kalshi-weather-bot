# Range-Scalp Bot

*Updated Sat Nov 28 10:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74540 | 65058 | 9482 (171) | 6 | $-19816.75 | -4.2% |
| **+10¢** | 55525 | 44447 | 11078 (217) | 8 | $-18447.23 | -5.3% |
| **+15¢** | 46489 | 34561 | 11928 (275) | 8 | $-16495.66 | -5.7% |
| **+20¢** | 41365 | 28804 | 12561 (343) | 8 | $-14902.34 | -5.7% |
| **+10¢ (15¢ stop)** | 90717 | 90497 | 220 (136) | 0 | $-33479.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 10:35 | +10 stop | SOL | UP | 0.48 | 0.32 | -1.94 |
| 11-28 10:35 | +15 | SOL | UP | 0.48 | open |  |
| 11-28 10:35 | +10 | SOL | UP | 0.48 | open |  |
| 11-28 10:35 | +5 | SOL | UP | 0.48 | 0.57 | 0.54 |
| 11-28 10:34 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 11-28 10:34 | +5 | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-28 10:34 | +10 stop | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-28 10:34 | +10 stop | ETH | DOWN | 0.53 | 0.76 | 1.99 |
| 11-28 10:34 | +10 stop | SOL | UP | 0.49 | 0.64 | 1.15 |
| 11-28 10:34 | +20 | SOL | UP | 0.49 | open |  |
| 11-28 10:34 | +15 | SOL | UP | 0.49 | 0.64 | 1.15 |
| 11-28 10:34 | +10 | SOL | UP | 0.49 | 0.64 | 1.15 |
| 11-28 10:34 | +5 | SOL | UP | 0.49 | 0.55 | 0.24 |
| 11-28 10:34 | +5 | XRP | UP | 0.62 | 0.71 | 0.58 |
| 11-28 10:33 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-28 10:33 | +10 stop | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-28 10:33 | +20 | ZEC | DOWN | 0.57 | 0.87 | 2.74 |
| 11-28 10:33 | +15 | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-28 10:33 | +10 | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-28 10:33 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-28 10:33 | +10 stop | BNB | UP | 0.66 | 0.50 | -1.94 |
| 11-28 10:33 | +10 | BNB | UP | 0.66 | open |  |
| 11-28 10:33 | +5 | BNB | UP | 0.66 | open |  |
| 11-28 10:31 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 11-28 10:31 | +20 | ETH | UP | 0.67 | open |  |
| 11-28 10:31 | +15 | ETH | UP | 0.67 | open |  |
| 11-28 10:31 | +10 | ETH | UP | 0.67 | open |  |
| 11-28 10:31 | +5 | ETH | UP | 0.67 | open |  |
| 11-28 10:31 | +10 stop | NEAR | UP | 0.61 | 0.44 | -2.07 |
| 11-28 10:31 | +20 | NEAR | UP | 0.61 | open |  |
| 11-28 10:31 | +15 | NEAR | UP | 0.61 | open |  |
| 11-28 10:31 | +10 | NEAR | UP | 0.61 | open |  |
| 11-28 10:31 | +5 | NEAR | UP | 0.61 | open |  |
| 11-28 10:30 | +10 stop | DOGE | UP | 0.61 | 0.44 | -2.05 |
| 11-28 10:30 | +20 | DOGE | UP | 0.61 | open |  |
| 11-28 10:30 | +15 | DOGE | UP | 0.61 | open |  |
| 11-28 10:30 | +10 | DOGE | UP | 0.61 | open |  |
| 11-28 10:30 | +5 | DOGE | UP | 0.61 | open |  |
| 11-28 10:30 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-28 10:30 | +20 | BNB | UP | 0.62 | open |  |
