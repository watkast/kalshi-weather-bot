# Range-Scalp Bot

*Updated Sat Nov 14 20:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59797 | 52175 | 7622 (107) | 7 | $-16170.84 | -4.3% |
| **+10¢** | 44668 | 35742 | 8926 (143) | 9 | $-15206.66 | -5.4% |
| **+15¢** | 37423 | 27798 | 9625 (180) | 9 | $-13839.64 | -5.9% |
| **+20¢** | 33341 | 23241 | 10100 (232) | 9 | $-12182.80 | -5.8% |
| **+10¢ (15¢ stop)** | 72775 | 72632 | 143 (82) | 3 | $-26760.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 20:09 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 11-14 20:08 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 11-14 20:08 | +10 | BTC | DOWN | 0.57 | open |  |
| 11-14 20:08 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 11-14 20:08 | +10 stop | SOL | DOWN | 0.53 | open |  |
| 11-14 20:07 | +10 stop | BTC | UP | 0.45 | 0.55 | 0.64 |
| 11-14 20:07 | +20 | BTC | UP | 0.45 | open |  |
| 11-14 20:07 | +15 | BTC | UP | 0.45 | open |  |
| 11-14 20:07 | +10 | BTC | UP | 0.45 | 0.55 | 0.64 |
| 11-14 20:07 | +5 | BTC | UP | 0.45 | 0.55 | 0.64 |
| 11-14 20:07 | +10 stop | ZEC | DOWN | 0.40 | 0.55 | 1.15 |
| 11-14 20:07 | +10 stop | ETH | DOWN | 0.56 | 0.69 | 0.97 |
| 11-14 20:06 | +10 stop | ZEC | UP | 0.53 | 0.36 | -2.05 |
| 11-14 20:05 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-14 20:05 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 11-14 20:05 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-14 20:05 | +10 stop | BNB | UP | 0.66 | 0.48 | -2.11 |
| 11-14 20:05 | +20 | BNB | UP | 0.66 | open |  |
| 11-14 20:05 | +15 | BNB | UP | 0.66 | open |  |
| 11-14 20:05 | +10 | BNB | UP | 0.66 | open |  |
| 11-14 20:05 | +5 | BNB | UP | 0.69 | open |  |
| 11-14 20:05 | +10 stop | DOGE | UP | 0.66 | 0.48 | -2.14 |
| 11-14 20:05 | +20 | DOGE | UP | 0.66 | open |  |
| 11-14 20:05 | +15 | DOGE | UP | 0.66 | open |  |
| 11-14 20:05 | +10 | DOGE | UP | 0.66 | open |  |
| 11-14 20:05 | +5 | DOGE | UP | 0.66 | open |  |
| 11-14 20:05 | +5 | SOL | UP | 0.63 | open |  |
| 11-14 20:05 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-14 20:04 | +5 | XRP | UP | 0.41 | 0.57 | 1.25 |
| 11-14 20:04 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 11-14 20:04 | +20 | ZEC | UP | 0.67 | open |  |
| 11-14 20:04 | +15 | ZEC | UP | 0.67 | open |  |
| 11-14 20:04 | +10 | ZEC | UP | 0.67 | open |  |
| 11-14 20:04 | +5 | ZEC | UP | 0.67 | open |  |
| 11-14 20:04 | +10 stop | ETH | UP | 0.68 | 0.50 | -2.14 |
| 11-14 20:04 | +20 | ETH | UP | 0.69 | open |  |
| 11-14 20:04 | +15 | ETH | UP | 0.69 | open |  |
| 11-14 20:04 | +10 | ETH | UP | 0.69 | open |  |
| 11-14 20:04 | +5 | ETH | UP | 0.69 | open |  |
| 11-14 20:04 | +10 stop | SOL | UP | 0.67 | 0.45 | -2.54 |
