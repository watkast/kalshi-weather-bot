# Range-Scalp Bot

*Updated Fri Nov 27 07:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73495 | 64138 | 9357 (165) | 7 | $-19604.07 | -4.2% |
| **+10¢** | 54765 | 43838 | 10927 (210) | 6 | $-18241.77 | -5.3% |
| **+15¢** | 45861 | 34092 | 11769 (268) | 8 | $-16337.66 | -5.7% |
| **+20¢** | 40814 | 28422 | 12392 (334) | 9 | $-14740.25 | -5.8% |
| **+10¢ (15¢ stop)** | 89512 | 89300 | 212 (129) | 4 | $-33130.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 07:04 | +5 | BTC | UP | 0.70 | open |  |
| 11-27 07:03 | +5 | BNB | UP | 0.71 | open |  |
| 11-27 07:03 | +10 stop | SOL | UP | 0.62 | open |  |
| 11-27 07:03 | +5 | SOL | UP | 0.62 | open |  |
| 11-27 07:03 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-27 07:03 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 11-27 07:03 | +10 stop | HYPE | UP | 0.68 | open |  |
| 11-27 07:02 | +10 stop | BNB | UP | 0.57 | 0.69 | 0.87 |
| 11-27 07:02 | +10 | BNB | UP | 0.57 | 0.69 | 0.87 |
| 11-27 07:02 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 11-27 07:02 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-27 07:02 | +20 | DOGE | UP | 0.61 | open |  |
| 11-27 07:02 | +15 | DOGE | UP | 0.61 | open |  |
| 11-27 07:02 | +10 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-27 07:02 | +5 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-27 07:02 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:02 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-27 07:02 | +5 | SOL | DOWN | 0.47 | 0.57 | 0.64 |
| 11-27 07:02 | +5 | BTC | DOWN | 0.48 | 0.66 | 1.46 |
| 11-27 07:02 | +10 stop | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-27 07:02 | +20 | BNB | DOWN | 0.45 | open |  |
| 11-27 07:02 | +15 | BNB | DOWN | 0.45 | open |  |
| 11-27 07:02 | +10 | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-27 07:02 | +5 | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-27 07:01 | +10 stop | NEAR | UP | 0.64 | 0.77 | 1.05 |
| 11-27 07:01 | +20 | NEAR | UP | 0.64 | open |  |
| 11-27 07:01 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-27 07:01 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 11-27 07:01 | +5 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 11-27 07:01 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:01 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:01 | +15 | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:01 | +10 | ZEC | DOWN | 0.65 | open |  |
| 11-27 07:01 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-27 07:01 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 11-27 07:01 | +10 stop | ETH | DOWN | 0.64 | 0.46 | -2.15 |
| 11-27 07:01 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-27 07:01 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-27 07:01 | +10 | ETH | DOWN | 0.63 | open |  |
| 11-27 07:01 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
