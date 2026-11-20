# Range-Scalp Bot

*Updated Fri Nov 20 07:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66044 | 57635 | 8409 (125) | 1 | $-17803.71 | -4.3% |
| **+10¢** | 49320 | 39488 | 9832 (166) | 4 | $-16593.97 | -5.4% |
| **+15¢** | 41365 | 30759 | 10606 (213) | 5 | $-14960.69 | -5.8% |
| **+20¢** | 36826 | 25688 | 11138 (269) | 6 | $-13254.12 | -5.7% |
| **+10¢ (15¢ stop)** | 80424 | 80260 | 164 (98) | 1 | $-29655.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 07:38 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
| 11-20 07:38 | +15 | ETH | UP | 0.54 | open |  |
| 11-20 07:38 | +10 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-20 07:38 | +5 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-20 07:38 | +10 stop | BTC | UP | 0.43 | 0.56 | 0.94 |
| 11-20 07:38 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-20 07:38 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-20 07:38 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-20 07:38 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-20 07:38 | +5 | BNB | DOWN | 0.70 | 0.78 | 0.50 |
| 11-20 07:37 | +10 stop | NEAR | DOWN | 0.54 | 0.36 | -2.15 |
| 11-20 07:37 | +10 stop | BTC | DOWN | 0.67 | 0.45 | -2.54 |
| 11-20 07:37 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-20 07:37 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-20 07:37 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-20 07:37 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-20 07:37 | +10 stop | ETH | DOWN | 0.63 | 0.24 | -4.20 |
| 11-20 07:34 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-20 07:33 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-20 07:33 | +5 | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-20 07:33 | +10 stop | HYPE | DOWN | 0.64 | 0.85 | 1.84 |
| 11-20 07:33 | +10 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-20 07:33 | +5 | HYPE | DOWN | 0.67 | 0.85 | 1.57 |
| 11-20 07:33 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 11-20 07:32 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-20 07:32 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-20 07:32 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-20 07:32 | +15 | SOL | DOWN | 0.68 | 0.85 | 1.45 |
| 11-20 07:32 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-20 07:32 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 07:32 | +5 | NEAR | UP | 0.54 | 0.62 | 0.45 |
| 11-20 07:32 | +5 | ZEC | UP | 0.50 | 0.60 | 0.65 |
| 11-20 07:32 | +10 stop | ETH | UP | 0.59 | 0.35 | -2.73 |
| 11-20 07:32 | +20 | ETH | UP | 0.59 | open |  |
| 11-20 07:32 | +15 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 11-20 07:32 | +10 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 11-20 07:32 | +5 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 11-20 07:31 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 11-20 07:31 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 11-20 07:31 | +15 | XRP | DOWN | 0.65 | 0.83 | 1.54 |
