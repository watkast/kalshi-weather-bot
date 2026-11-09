# Range-Scalp Bot

*Updated Mon Nov 09 06:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53434 | 46591 | 6843 (85) | 2 | $-14751.11 | -4.4% |
| **+10¢** | 39912 | 31930 | 7982 (110) | 4 | $-13754.53 | -5.5% |
| **+15¢** | 33443 | 24842 | 8601 (141) | 7 | $-12556.72 | -6.0% |
| **+20¢** | 29757 | 20737 | 9020 (186) | 8 | $-11064.36 | -5.9% |
| **+10¢ (15¢ stop)** | 65107 | 65001 | 106 (63) | 3 | $-24116.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 06:37 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-09 06:36 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 11-09 06:36 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-09 06:36 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-09 06:36 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-09 06:36 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-09 06:35 | +5 | ZEC | UP | 0.64 | 0.71 | 0.38 |
| 11-09 06:33 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.07 |
| 11-09 06:33 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-09 06:33 | +15 | BNB | DOWN | 0.70 | open |  |
| 11-09 06:33 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.07 |
| 11-09 06:33 | +5 | BNB | DOWN | 0.70 | 0.78 | 0.54 |
| 11-09 06:33 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-09 06:33 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 11-09 06:33 | +5 | HYPE | DOWN | 0.58 | 0.66 | 0.46 |
| 11-09 06:33 | +10 stop | NEAR | UP | 0.71 | open |  |
| 11-09 06:33 | +20 | NEAR | UP | 0.71 | open |  |
| 11-09 06:33 | +15 | NEAR | UP | 0.70 | open |  |
| 11-09 06:33 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-09 06:33 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 11-09 06:32 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.08 |
| 11-09 06:32 | +20 | XRP | DOWN | 0.62 | 0.85 | 1.99 |
| 11-09 06:32 | +15 | XRP | DOWN | 0.62 | 0.85 | 1.99 |
| 11-09 06:32 | +10 | XRP | DOWN | 0.62 | 0.77 | 1.15 |
| 11-09 06:32 | +5 | XRP | DOWN | 0.62 | 0.77 | 1.15 |
| 11-09 06:32 | +5 | ETH | DOWN | 0.56 | 0.76 | 1.69 |
| 11-09 06:31 | +10 stop | DOGE | UP | 0.53 | 0.30 | -2.63 |
| 11-09 06:31 | +20 | DOGE | UP | 0.53 | open |  |
| 11-09 06:31 | +15 | DOGE | UP | 0.53 | open |  |
| 11-09 06:31 | +10 | DOGE | UP | 0.53 | open |  |
| 11-09 06:31 | +5 | DOGE | UP | 0.53 | open |  |
| 11-09 06:31 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-09 06:31 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-09 06:31 | +15 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-09 06:31 | +10 | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-09 06:31 | +5 | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 06:31 | +10 stop | SOL | UP | 0.64 | 0.35 | -3.23 |
| 11-09 06:31 | +20 | SOL | UP | 0.64 | open |  |
| 11-09 06:31 | +15 | SOL | UP | 0.64 | open |  |
| 11-09 06:31 | +10 | SOL | UP | 0.65 | open |  |
