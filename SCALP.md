# Range-Scalp Bot

*Updated Sat Nov 07 23:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51637 | 45023 | 6614 (80) | 7 | $-14328.61 | -4.4% |
| **+10¢** | 38530 | 30817 | 7713 (106) | 7 | $-13353.25 | -5.5% |
| **+15¢** | 32265 | 23952 | 8313 (135) | 7 | $-12258.51 | -6.1% |
| **+20¢** | 28698 | 19982 | 8716 (180) | 8 | $-10823.01 | -6.0% |
| **+10¢ (15¢ stop)** | 62876 | 62773 | 103 (61) | 2 | $-23297.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 23:02 | +20 | ZEC | DOWN | 0.54 | open |  |
| 11-07 23:02 | +15 | ZEC | DOWN | 0.54 | open |  |
| 11-07 23:02 | +10 stop | SOL | DOWN | 0.57 | 0.27 | -3.32 |
| 11-07 23:02 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:02 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-07 23:01 | +10 stop | XRP | DOWN | 0.63 | 0.45 | -2.15 |
| 11-07 23:01 | +20 | XRP | DOWN | 0.63 | open |  |
| 11-07 23:01 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-07 23:01 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-07 23:01 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-07 23:01 | +10 stop | BNB | DOWN | 0.69 | 0.48 | -2.43 |
| 11-07 23:01 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-07 23:01 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-07 23:01 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-07 23:01 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-07 23:01 | +10 stop | NEAR | UP | 0.61 | 0.77 | 1.25 |
| 11-07 23:01 | +20 | NEAR | UP | 0.61 | open |  |
| 11-07 23:01 | +15 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-07 23:01 | +10 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 11-07 23:01 | +5 | NEAR | UP | 0.60 | 0.69 | 0.53 |
| 11-07 23:01 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 11-07 23:01 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-07 23:01 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-07 23:01 | +10 | DOGE | DOWN | 0.65 | open |  |
| 11-07 23:01 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-07 23:01 | +10 stop | ZEC | DOWN | 0.70 | 0.53 | -2.03 |
| 11-07 23:01 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-07 23:01 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-07 23:01 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-07 23:01 | +10 stop | ETH | DOWN | 0.58 | open |  |
| 11-07 23:01 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-07 23:01 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-07 23:00 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 11-07 23:00 | +20 | BTC | DOWN | 0.58 | open |  |
| 11-07 23:00 | +15 | BTC | DOWN | 0.59 | open |  |
| 11-07 23:00 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-07 23:00 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-07 23:00 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
