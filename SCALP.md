# Range-Scalp Bot

*Updated Sat Nov 14 17:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59639 | 52040 | 7599 (107) | 6 | $-16103.62 | -4.3% |
| **+10¢** | 44552 | 35653 | 8899 (143) | 6 | $-15130.60 | -5.4% |
| **+15¢** | 37328 | 27732 | 9596 (180) | 7 | $-13757.72 | -5.9% |
| **+20¢** | 33248 | 23177 | 10071 (232) | 8 | $-12133.26 | -5.8% |
| **+10¢ (15¢ stop)** | 72566 | 72423 | 143 (82) | 4 | $-26692.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 17:36 | +10 stop | SOL | UP | 0.48 | open |  |
| 11-14 17:35 | +10 stop | ETH | UP | 0.57 | open |  |
| 11-14 17:35 | +15 | ETH | UP | 0.57 | open |  |
| 11-14 17:35 | +10 stop | ETH | DOWN | 0.47 | 0.57 | 0.64 |
| 11-14 17:35 | +5 | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-14 17:34 | +10 stop | BNB | UP | 0.62 | 0.75 | 0.99 |
| 11-14 17:34 | +20 | BNB | UP | 0.62 | open |  |
| 11-14 17:34 | +15 | BNB | UP | 0.62 | open |  |
| 11-14 17:34 | +10 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 11-14 17:34 | +5 | BNB | UP | 0.62 | 0.75 | 0.99 |
| 11-14 17:34 | +10 stop | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 11-14 17:34 | +10 | ZEC | UP | 0.59 | 0.74 | 1.19 |
| 11-14 17:34 | +5 | ZEC | UP | 0.59 | 0.66 | 0.37 |
| 11-14 17:34 | +10 stop | NEAR | UP | 0.64 | open |  |
| 11-14 17:34 | +15 | NEAR | UP | 0.64 | open |  |
| 11-14 17:34 | +10 | NEAR | UP | 0.64 | open |  |
| 11-14 17:34 | +10 | DOGE | UP | 0.65 | open |  |
| 11-14 17:34 | +10 stop | XRP | UP | 0.47 | 0.58 | 0.74 |
| 11-14 17:33 | +5 | DOGE | UP | 0.69 | open |  |
| 11-14 17:33 | +10 stop | BTC | UP | 0.56 | 0.68 | 0.86 |
| 11-14 17:33 | +10 stop | SOL | UP | 0.62 | 0.41 | -2.44 |
| 11-14 17:33 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-14 17:33 | +10 stop | ETH | UP | 0.59 | 0.44 | -1.85 |
| 11-14 17:33 | +10 | ETH | UP | 0.59 | open |  |
| 11-14 17:33 | +5 | ETH | UP | 0.60 | open |  |
| 11-14 17:33 | +10 stop | ETH | DOWN | 0.42 | 0.54 | 0.84 |
| 11-14 17:33 | +15 | ETH | DOWN | 0.42 | 0.57 | 1.14 |
| 11-14 17:33 | +10 | ETH | DOWN | 0.42 | 0.54 | 0.84 |
| 11-14 17:33 | +5 | ETH | DOWN | 0.43 | 0.54 | 0.74 |
| 11-14 17:33 | +10 stop | BTC | DOWN | 0.58 | 0.41 | -2.05 |
| 11-14 17:33 | +10 | BTC | DOWN | 0.58 | open |  |
| 11-14 17:32 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-14 17:32 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 11-14 17:32 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-14 17:32 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-14 17:32 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-14 17:32 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-14 17:32 | +5 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-14 17:32 | +10 stop | SOL | DOWN | 0.67 | 0.37 | -3.33 |
| 11-14 17:32 | +20 | SOL | DOWN | 0.67 | open |  |
